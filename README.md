# ⏱️ Timing Intuition Builder

**Build muscle memory for latency thresholds through visual repetition.**

## What is this?

An interactive training tool that helps developers and engineers internalize what different response times actually *feel* like. By watching progress bars fill at different speeds repeatedly, you develop instinctive recognition of latency ranges—anchored to physical sensations like eye movements and blinks.

## Why does this matter?

Engineers often make performance decisions based on numbers alone. But understanding *viscerally* that 100ms is one blink while 500ms is five blinks helps you:
- Set better SLOs and performance budgets
- Make faster architectural decisions during design reviews
- Debug latency issues with better intuition about "where to look"
- Communicate performance requirements more effectively

## Live Demo

**🔗 [Try it now](https://tanaysd.github.io/timing-intuition/)**

## Timing Thresholds

| Duration | Physical Anchor | Technical Meaning |
|----------|----------------|-------------------|
| 10ms | Eye saccade | Animation frame (fastest human motion) |
| 100ms | 1 blink | Instant feedback threshold |
| 500ms | 5 blinks | Noticeable delay (needs acknowledgment) |
| 1000ms | 10 blinks | Flow threshold (maintains thought continuity) |
| 5000ms | 50 blinks | Patience limit (maximum tolerable wait) |

## How to Use

1. **Set iterations** (default: 5) — more repetitions = stronger intuition
2. **Click Start** — watch all five timers fill at their respective speeds
3. **Observe the physical anchors** — count blinks, feel the eye movements
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
