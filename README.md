# memory_profiling_in_python

## Why Memory Profiling?

- Inefficient memory utilization make the applications' performance drop, and even make it crash.


## Challenges of Memory Profiling in Python

- Abstract layer for memory manipulation (e.g. pymalloc).
- Extension modules (e.g. C/C++ functions in numpy).

## Prerequisites

- Frames
- PyMalloc

## Python Frames
```bash
$ poetry run python memory_profiling_in_python/01_python_frames.py
```

## Inspecting Abstract Layer (PyMalloc)

### Without PyMalloc Tracking

```bash
$ poetry run memray run -fo memray.bin memory_profiling_in_python/02_track_pymalloc.py

$ poetry run memray flamegraph -fo memray.html memray.bin

$ open memray.html
```

### With PyMalloc Tracking
```bash
$ poetry run memray run -fo memray.bin --trace-python-allocators memory_profiling_in_python/02_track_pymalloc.py

$ poetry run memray flamegraph -fo memray.html memray.bin

$ open memray.html
```

## Native Tracking with Mandelbrot

### Without Native Tracking
```bash
$ poetry run memray run -fo memray.bin memory_profiling_in_python/03_native_tracking.py

$ poetry run memray flamegraph -fo memray.html memray.bin

$ open memray.html
```

### With Native Tracking
```bash
$ poetry run memray run -fo memray.bin --native memory_profiling_in_python/03_native_tracking.py

$ poetry run memray flamegraph -fo memray.html memray.bin

$ open memray.html
```

## Multiprocessing

### Without Fork Following
```bash
$ poetry run memray run -fo memray.bin memory_profiling_in_python/04_multiprocessing_gunicorn.py

$ poetry run memray flamegraph -fo memray.html memray.bin

$ open memray.html
```

### With Fork Following
```bash
$ poetry run memray run -fo memray.bin --follow-fork memory_profiling_in_python/04_multiprocessing_gunicorn.py

$ poetry run memray flamegraph -fo memray.html memray.bin

$ open memray.html
```

## Summarize Temporary Allocations

```bash
$ poetry run memray run -fo memray.bin memory_profiling_in_python/05_temporary_allocation.py

$ poetry run memray summary memray.bin --temporary-allocations
```

## Attach to Running Process

```bash
$ poetry run python memory_profiling_in_python/06_attach_to_process.py

$ poetry run memray attach ${YOUR_UVICORN_PROCESS_ID}

```

## Context Manager

```bash
$ poetry run python memory_profiling_in_python/07_context_manager.py

$ poetry run memray summary memray.bin --temporary-allocations
```