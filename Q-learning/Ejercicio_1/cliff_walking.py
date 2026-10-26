#!/usr/bin/env python3
"""Ejercicio 1: Q-learning tabular en Cliff Walking 4x12"""

from __future__ import annotations

import argparse
import csv
import random
from dataclasses import dataclass, replace
from pathlib import Path

State = tuple[int, int]
QTable = dict[State, dict[str, float]]

DELTAS: dict[str, tuple[int, int]] = {
    "N": (-1, 0),
    "E": (0, 1),
    "S": (1, 0),
    "W": (0, -1),
}

ARROWS: dict[str, str] = {
    "N": "↑",
    "E": "→",
    "S": "↓",
    "W": "←",
}


@dataclass(frozen=True)
class CliffEnv:
    name: str = "Cliff Walking 4×12 (Sutton & Barto)"
    rows: int = 4
    cols: int = 12
    start: State = (3, 0)
    goal: State = (3, 11)
    cliffs: frozenset[State] = frozenset((3, c) for c in range(1, 11))
    actions: tuple[str, ...] = ("N", "E", "S", "W")
    step_reward: float = -1.0
    goal_reward: float = -1.0
    cliff_reward: float = -100.0
    alpha: float = 0.5
    gamma: float = 1.0
    epsilon: float = 0.1
    episodes: int = 500
    max_steps: int = 200
    seed: int = 1

    def states(self) -> list[State]:
        return [(r, c) for r in range(self.rows) for c in range(self.cols)]

    def is_terminal(self, s: State) -> bool:
        return s == self.goal

    def step(self, s: State, a: str) -> tuple[State, float, bool]:
        dr, dc = DELTAS[a]
        nr = max(0, min(self.rows - 1, s[0] + dr))
        nc = max(0, min(self.cols - 1, s[1] + dc))
        ns: State = (nr, nc)

        if ns in self.cliffs:
            return self.start, self.cliff_reward, False
        if ns == self.goal:
            return ns, self.goal_reward, True
        return ns, self.step_reward, False


def empty_q(env: CliffEnv) -> QTable:
    """Inicializa Q(s, a) = 0.0 para cada estado y acción."""
    return {
        s: {a: 0.0 for a in env.actions}
        for s in env.states()
        if not env.is_terminal(s) and s not in env.cliffs
    }


def argmax_action(env: CliffEnv, Q: QTable, s: State) -> str:
    """Elige la acción con mayor Q(s, a). Empates siguen el orden [N, E, S, W]."""
    best_a = env.actions[0]
    best_val = Q[s][best_a]
    for a in env.actions[1:]:
        if Q[s][a] > best_val:
            best_val = Q[s][a]
            best_a = a
    return best_a


def epsilon_greedy(
    env: CliffEnv, Q: QTable, s: State, rng: random.Random, epsilon: float
) -> str:
    """Con probabilidad ε elige al azar; si no, elige argmax_a Q(s, a)."""
    if rng.random() < epsilon:
        return rng.choice(env.actions)
    return argmax_action(env, Q, s)


def td_target_q(
    env: CliffEnv, Q: QTable, r: float, ns: State, terminal: bool
) -> float:
    """Blanco off-policy de Q-learning: r + γ max_a' Q(s', a')."""
    if terminal or env.is_terminal(ns):
        return r
    max_next = max(Q[ns][a] for a in env.actions)
    return r + env.gamma * max_next


def apply_update(
    env: CliffEnv, Q: QTable, s: State, a: str, target: float
) -> None:
    """Regla de Watkins: Q(s, a) ← Q(s, a) + α [ target − Q(s, a) ]."""
    Q[s][a] += env.alpha * (target - Q[s][a])


def train(
    env: CliffEnv, rng: random.Random
) -> tuple[QTable, list[float]]:
    """Entrena Q-learning durante env.episodes episodios."""
    Q = empty_q(env)
    returns: list[float] = []

    for _ in range(env.episodes):
        s = env.start
        ep_return = 0.0
        for _step in range(env.max_steps):
            a = epsilon_greedy(env, Q, s, rng, env.epsilon)
            ns, r, done = env.step(s, a)
            target = td_target_q(env, Q, r, ns, done)
            apply_update(env, Q, s, a, target)
            s = ns
            ep_return += r
            if done:
                break
        returns.append(ep_return)

    return Q, returns


def greedy_rollout(
    env: CliffEnv, Q: QTable
) -> tuple[list[State], list[str], float]:
    """Evalúa la política greedy (ε = 0) desde S hasta G."""
    s = env.start
    states_path: list[State] = [s]
    actions_path: list[str] = []
    total_return = 0.0

    for _ in range(env.max_steps):
        a = argmax_action(env, Q, s)
        ns, r, done = env.step(s, a)
        actions_path.append(a)
        states_path.append(ns)
        total_return += r
        s = ns
        if done:
            break

    return states_path, actions_path, total_return


def moving_average(returns: list[float], window: int = 10) -> list[float]:
    """Calcula la media móvil de ventana `window` para cada episodio."""
    ma: list[float] = []
    for i in range(len(returns)):
        start_idx = max(0, i + 1 - window)
        segment = returns[start_idx : i + 1]
        ma.append(sum(segment) / len(segment))
    return ma


def format_env(env: CliffEnv) -> str:
    lines = [
        f"{env.name}  (kind = grid, {env.rows}×{env.cols})",
        f"start = {env.start}    goal = {env.goal}    cliffs = (3,1)..(3,10) -> reset to S",
        f"actions = {list(env.actions)} (tie-break order)",
        f"r_step = {env.step_reward:g}    r_cliff = {env.cliff_reward:g}    r_goal = {env.goal_reward:g}",
        f"α = {env.alpha:g}    γ = {env.gamma:g}    ε = {env.epsilon:g}    "
        f"episodes = {env.episodes}    max_steps = {env.max_steps}    seed = {env.seed}",
    ]
    return "\n".join(lines)


def format_grid_policy(env: CliffEnv, Q: QTable) -> str:
    header = "row\\col " + " ".join(f"{c:2d}" for c in range(env.cols))
    lines = [header]
    for r in range(env.rows):
        row_cells = []
        for c in range(env.cols):
            s = (r, c)
            if s == env.goal:
                cell = " G"
            elif s in env.cliffs:
                cell = " C"
            else:
                best_a = argmax_action(env, Q, s)
                cell = f" {ARROWS[best_a]}"
            row_cells.append(cell)
        lines.append(f"{r:<7d} " + " ".join(row_cells))
    return "\n".join(lines)


def format_returns(returns: list[float], window: int = 10) -> str:
    ma = moving_average(returns, window)
    lines = [
        f"{'Episodios':>12}  {'Retorno medio':>15}  {'Mín':>8}  {'Máx':>8}  {'Media móvil (últ. 10)':>22}"
    ]
    blocks = [
        (1, 10),
        (11, 50),
        (51, 100),
        (101, 200),
        (201, 300),
        (301, 400),
        (401, 500),
    ]
    for start_ep, end_ep in blocks:
        if end_ep > len(returns):
            break
        seg = returns[start_ep - 1 : end_ep]
        lines.append(
            f"{f'{start_ep}..{end_ep}':>12}  {sum(seg)/len(seg):15.2f}  "
            f"{min(seg):8.0f}  {max(seg):8.0f}  {ma[end_ep - 1]:22.2f}"
        )
    return "\n".join(lines)


def format_ascii_curve(returns: list[float], window: int = 10) -> str:
    """Dibuja la curva de media móvil (500 episodios mapeados a 50 columnas)."""
    ma = moving_average(returns, window)
    cols = 50
    step = max(1, len(ma) // cols)
    sampled = [sum(ma[i : i + step]) / len(ma[i : i + step]) for i in range(0, len(ma), step)][:cols]

    y_min, y_max = -120.0, -10.0
    height = 10
    grid = [[" " for _ in range(len(sampled))] for _ in range(height)]

    for c, val in enumerate(sampled):
        clamped = max(y_min, min(y_max, val))
        norm = (clamped - y_min) / (y_max - y_min)
        r = height - 1 - int(round(norm * (height - 1)))
        grid[r][c] = "•"

    lines = []
    for r in range(height):
        y_val = y_max - (r / (height - 1)) * (y_max - y_min)
        lines.append(f"{y_val:6.0f} | " + "".join(grid[r]))
    lines.append("       +" + "-" * len(sampled))
    lines.append("Ep.      1        100       200       300       400      500")
    return "\n".join(lines)


def save_returns_csv(returns: list[float], path: Path, window: int = 10) -> None:
    """Guarda los 500 episodios y su media móvil en un archivo CSV."""
    ma = moving_average(returns, window)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["episodio", "recompensa", f"media_movil_{window}"])
        for i, (ret, m) in enumerate(zip(returns, ma), 1):
            writer.writerow([i, f"{ret:.1f}", f"{m:.2f}"])


def verify_transitions(env: CliffEnv) -> None:
    assert env.step((3, 0), "N") == ((2, 0), -1.0, False)
    assert env.step((3, 0), "E") == ((3, 0), -100.0, False)
    assert env.step((2, 11), "S") == ((3, 11), -1.0, True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Train Q-learning on 4x12 Cliff Walking.")
    parser.add_argument("--seed", type=int, default=None, help="Random seed")
    parser.add_argument("--episodes", type=int, default=None, help="Number of episodes")
    parser.add_argument("--epsilon", type=float, default=None, help="Exploration rate")
    parser.add_argument("--alpha", type=float, default=None, help="Learning rate")
    parser.add_argument("--gamma", type=float, default=None, help="Discount factor")
    args = parser.parse_args()

    env = CliffEnv()
    env = replace(
        env,
        seed=args.seed if args.seed is not None else env.seed,
        episodes=args.episodes if args.episodes is not None else env.episodes,
        epsilon=args.epsilon if args.epsilon is not None else env.epsilon,
        alpha=args.alpha if args.alpha is not None else env.alpha,
        gamma=args.gamma if args.gamma is not None else env.gamma,
    )

    verify_transitions(env)
    rng = random.Random(env.seed)

    print(format_env(env))
    print()
    print("method = q-learning (off-policy)    behaviour = ε-greedy")
    print()

    Q, returns = train(env, rng)

    print("Greedy policy (arrows)")
    print("-" * 72)
    print(format_grid_policy(env, Q))
    print()

    states_path, actions_path, g_return = greedy_rollout(env, Q)
    print("Greedy rollout from S (ε = 0)")
    print("-" * 72)
    print(f"Actions ({len(actions_path)} steps): {' -> '.join(actions_path)}")
    print(f"States:  {' -> '.join(str(s) for s in states_path)}")
    print(f"greedy return from start (ε = 0): {g_return:g}")
    print()

    print("Training returns summary (ε = 0.1)")
    print("-" * 72)
    print(format_returns(returns))
    print()

    print("Moving average curve (window = 10, clipped at -120)")
    print("-" * 72)
    print(format_ascii_curve(returns, window=10))
    print()

    csv_path = Path(__file__).resolve().parent / "recompensas_500_episodios.csv"
    save_returns_csv(returns, csv_path, window=10)
    print(f"Full 500-episode series saved to: {csv_path.name}")


if __name__ == "__main__":
    main()