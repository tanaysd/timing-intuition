#!/usr/bin/env python3
"""
Timing Intuition Builder - Visual comparison of common time durations.

Usage:
    python timing_intuition.py [--iterations N]

Default: 5 iterations
"""

import tkinter as tk
from tkinter import ttk
import time
import argparse
import threading


class TimingIntuitionApp:
    """GUI app to visualize and build intuition for different time durations."""

    # Time slices in milliseconds with colors and descriptions
    TIME_SLICES = [
        (9, "#FF6B6B", "Instant (9ms)", "Frame render time"),
        (50, "#4ECDC4", "Quick (50ms)", "Snappy UI response"),
        (200, "#45B7D1", "Perceptible (200ms)", "Button click feedback"),
        (750, "#FFA07A", "Noticeable (750ms)", "API call"),
        (1000, "#98D8C8", "1 Second", "Human reaction time"),
        (5000, "#C7CEEA", "5 Seconds", "User patience limit"),
    ]

    def __init__(self, root, iterations=5):
        self.root = root
        self.iterations = iterations
        self.current_iteration = 0
        self.running = False

        self.root.title("Timing Intuition Builder")
        self.root.geometry("800x600")
        self.root.configure(bg="#1a1a1a")

        self._setup_ui()

    def _setup_ui(self):
        """Set up the UI components."""
        # Header
        header = tk.Frame(self.root, bg="#1a1a1a")
        header.pack(pady=20)

        self.title_label = tk.Label(
            header,
            text="Timing Intuition Builder",
            font=("Helvetica", 24, "bold"),
            bg="#1a1a1a",
            fg="#ffffff"
        )
        self.title_label.pack()

        self.iteration_label = tk.Label(
            header,
            text=f"Iteration 0/{self.iterations}",
            font=("Helvetica", 14),
            bg="#1a1a1a",
            fg="#888888"
        )
        self.iteration_label.pack(pady=5)

        # Progress bars container
        self.progress_frame = tk.Frame(self.root, bg="#1a1a1a")
        self.progress_frame.pack(pady=20, padx=40, fill=tk.BOTH, expand=True)

        self.progress_bars = []
        self.time_labels = []

        for duration_ms, color, label, description in self.TIME_SLICES:
            # Container for each timer
            timer_frame = tk.Frame(self.progress_frame, bg="#1a1a1a")
            timer_frame.pack(fill=tk.X, pady=10)

            # Label frame
            label_frame = tk.Frame(timer_frame, bg="#1a1a1a")
            label_frame.pack(fill=tk.X, pady=5)

            # Main label
            main_label = tk.Label(
                label_frame,
                text=f"{label} - {description}",
                font=("Helvetica", 12, "bold"),
                bg="#1a1a1a",
                fg=color,
                anchor="w"
            )
            main_label.pack(side=tk.LEFT)

            # Time remaining label
            time_label = tk.Label(
                label_frame,
                text=f"{duration_ms}ms",
                font=("Helvetica", 11),
                bg="#1a1a1a",
                fg="#888888",
                anchor="e"
            )
            time_label.pack(side=tk.RIGHT)
            self.time_labels.append(time_label)

            # Progress bar
            style = ttk.Style()
            style.theme_use('default')
            style.configure(
                f"custom{duration_ms}.Horizontal.TProgressbar",
                troughcolor='#333333',
                background=color,
                thickness=30
            )

            progress = ttk.Progressbar(
                timer_frame,
                style=f"custom{duration_ms}.Horizontal.TProgressbar",
                orient=tk.HORIZONTAL,
                length=700,
                mode='determinate',
                maximum=100
            )
            progress.pack(fill=tk.X)
            self.progress_bars.append((progress, duration_ms))

        # Control buttons
        button_frame = tk.Frame(self.root, bg="#1a1a1a")
        button_frame.pack(pady=20)

        self.start_button = tk.Button(
            button_frame,
            text="Start",
            font=("Helvetica", 14, "bold"),
            bg="#4ECDC4",
            fg="#ffffff",
            command=self.start,
            padx=30,
            pady=10,
            relief=tk.FLAT,
            cursor="hand2"
        )
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(
            button_frame,
            text="Reset",
            font=("Helvetica", 14, "bold"),
            bg="#FF6B6B",
            fg="#ffffff",
            command=self.reset,
            padx=30,
            pady=10,
            relief=tk.FLAT,
            cursor="hand2"
        )
        self.reset_button.pack(side=tk.LEFT, padx=10)

    def start(self):
        """Start the timing visualization."""
        if not self.running:
            self.running = True
            self.start_button.config(state=tk.DISABLED)
            thread = threading.Thread(target=self._run_iterations, daemon=True)
            thread.start()

    def _run_iterations(self):
        """Run all iterations of the timing visualization."""
        for i in range(self.iterations):
            self.current_iteration = i + 1
            self.root.after(0, self._update_iteration_label)
            self._run_single_iteration()

            # Brief pause between iterations (except after last one)
            if i < self.iterations - 1:
                time.sleep(0.5)

        # Re-enable start button
        self.root.after(0, lambda: self.start_button.config(state=tk.NORMAL))
        self.running = False

    def _update_iteration_label(self):
        """Update the iteration counter label."""
        self.iteration_label.config(
            text=f"Iteration {self.current_iteration}/{self.iterations}"
        )

    def _run_single_iteration(self):
        """Run a single iteration showing all timers."""
        start_time = time.time()
        max_duration = max(d for d, _, _, _ in self.TIME_SLICES) / 1000.0

        # Update frequency: 16ms (~60 FPS)
        update_interval = 0.016

        while True:
            elapsed = time.time() - start_time

            if elapsed >= max_duration:
                # Ensure all bars reach 100%
                for i, (progress, duration_ms) in enumerate(self.progress_bars):
                    self.root.after(0, lambda p=progress: p.config(value=100))
                    self.root.after(0, lambda l=self.time_labels[i]: l.config(text="Done!"))
                break

            # Update each progress bar
            for i, (progress, duration_ms) in enumerate(self.progress_bars):
                duration_sec = duration_ms / 1000.0

                if elapsed >= duration_sec:
                    # Timer completed
                    percent = 100
                    remaining_text = "Done!"
                else:
                    # Timer in progress
                    percent = (elapsed / duration_sec) * 100
                    remaining_ms = int((duration_sec - elapsed) * 1000)
                    remaining_text = f"{remaining_ms}ms"

                # Schedule UI updates on main thread
                self.root.after(0, lambda p=progress, v=percent: p.config(value=v))
                self.root.after(0, lambda l=self.time_labels[i], t=remaining_text: l.config(text=t))

            time.sleep(update_interval)

    def reset(self):
        """Reset all progress bars and iteration counter."""
        self.current_iteration = 0
        self.iteration_label.config(text=f"Iteration 0/{self.iterations}")

        for i, (progress, duration_ms) in enumerate(self.progress_bars):
            progress.config(value=0)
            self.time_labels[i].config(text=f"{duration_ms}ms")


def main():
    parser = argparse.ArgumentParser(
        description="Build intuition for common time durations through visual comparison."
    )
    parser.add_argument(
        "--iterations",
        type=int,
        default=5,
        help="Number of iterations to run (default: 5)"
    )

    args = parser.parse_args()

    root = tk.Tk()
    app = TimingIntuitionApp(root, iterations=args.iterations)
    root.mainloop()


if __name__ == "__main__":
    main()
