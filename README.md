# memory_profiling_in_python

## Why Memory Profiling?

- Inefficient memory utilization make the applications' performance drop, and even make it crash.


## Challenges of Memory Profiling in Python

- Abstract layer for memory manipulation (e.g. pymalloc).
- Extension modules (e.g. C/C++ functions in numpy).

## Inspecting Abstract Layer (PyMalloc)

### Without PyMalloc Tracking
```bash
$ poetry run memray run -fo memray.bin memory_profiling_in_python/07_track_pymalloc.py

$ poetry run memray flamegraph -fo memray.html memray.bin

$ open memray.html
```

### With PyMalloc Tracking
```bash
$ poetry run memray run -fo memray.bin --trace-python-allocators memory_profiling_in_python/07_track_pymalloc.py

$ poetry run memray flamegraph -fo memray.html memray.bin

$ open memray.html
```

## Native Tracking with Mandelbrot

### Without Native Tracking
```bash
$ poetry run memray run -fo memray.bin memory_profiling_in_python/06_native_tracking.py

$ poetry run memray flamegraph -fo memray.html memray.bin

$ open memray.html
```

### With Native Tracking
```bash
$ poetry run memray run -fo memray.bin --native memory_profiling_in_python/06_native_tracking.py

$ poetry run memray flamegraph -fo memray.html memray.bin

$ open memray.html
```

## Multiprocessing

### Without Fork Following
```bash
$ poetry run memray run -fo memray.bin memory_profiling_in_python/06_native_tracking.py

$ poetry run memray flamegraph -fo memray.html memray.bin

$ open memray.html
```

### With Fork Following
```bash
$ poetry run memray run -fo memray.bin --follow-fork memory_profiling_in_python/06_native_tracking.py

$ poetry run memray flamegraph -fo memray.html memray.bin

$ open memray.html
```
