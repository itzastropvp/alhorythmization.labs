def read_in_chunks(total_size, chunk_size=1024):
    remaining = total_size
    while remaining > 0:
        current_chunk = min(chunk_size, remaining)
        yield "A" * current_chunk
        remaining -= current_chunk
print(list(read_in_chunks(2500, 1000)))