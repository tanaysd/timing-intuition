# ⏱️ Timing Intuition Builder

**Build muscle memory for latency thresholds through visual repetition.**

## What is this?

An interactive training tool that helps developers and engineers internalize what different response times actually *feel* like. By watching progress bars fill at different speeds repeatedly, you develop instinctive recognition of latency ranges—from "instant" (9ms) to "patience limit" (5 seconds).

## Why does this matter?

Engineers often make performance decisions based on numbers alone. But understanding *viscerally* that 50ms feels snappy while 200ms feels perceptible helps you:
- Set better SLOs and performance budgets
- Make faster architectural decisions during design reviews
- Debug latency issues with better intuition about "where to look"
- Communicate performance requirements more effectively

## Live Demo

**🔗 [Try it now](https://tanaysd.github.io/timing-intuition/)**

## Timing Thresholds

| Duration | Category | Description |
|----------|----------|-------------|
| 9ms | Instant | Single frame render time (60 FPS) |
| 50ms | Quick | Snappy UI response threshold |
| 200ms | Perceptible | Noticeable but acceptable delay |
| 750ms | Noticeable | Typical API call latency |
| 1000ms | 1 Second | Human reaction time baseline |
| 5000ms | Patience Limit | Maximum tolerable wait without feedback |

## How to Use

1. **Set iterations** (default: 5) — more repetitions = stronger intuition
2. **Click Start** — watch all six timers fill at their respective speeds
3. **Observe the differences** — focus on *feeling* the time passing, not just watching
4. **Repeat regularly** — like any skill, timing intuition requires practice

## The Science

This tool leverages **spaced repetition** and **visual anchoring** to help you build timing intuition:
- Multiple iterations reinforce the mental model
- Side-by-side comparison creates relative anchors
- Real-time visualization converts abstract numbers into felt experience

## Use Cases

- **Training new engineers** on performance expectations
- **Performance reviews** to align team on SLO targets
- **Interview prep** for system design discussions
- **Personal skill development** for senior/staff engineers

## Technical Details

- Pure HTML/CSS/JavaScript (no dependencies)
- Uses `requestAnimationFrame` for smooth 60 FPS updates
- Fully client-side, works offline after first load
- Responsive design, works on mobile and desktop

## Contributing

Ideas for improvement:
- Add custom time ranges
- Export timing data
- Gamification (test your intuition)
- Audio cues at completion

## License

MIT

---

*Built to help engineers develop better performance intuition through deliberate practice.*
