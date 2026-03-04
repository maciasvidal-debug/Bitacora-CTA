## 2026-03-04 - Optimize DOM and string manipulation in loops
**Learning:** Found multiple instances where DOM elements were appended individually in loops (e.g., table rows, dropdown options) causing unnecessary reflows/repaints, and strings were concatenated in loops for CSV generation, which can be inefficient due to multiple memory allocations.
**Action:** Always use DocumentFragment for batched DOM insertions within loops, and prefer array `.push()` combined with `.join()` for large string builder operations to ensure O(N) memory complexity rather than O(N^2).
