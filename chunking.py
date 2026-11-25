def text_splitter(text: str, chunk_size: int = 150, overlap: int = 30) -> list[str]:
    words = text.split()
    chunks = []
    current_chunk = []
    current_length = 0

    for word in words:
        # +1 accounts for the space between words
        if current_length + len(word) + 1 > chunk_size and current_chunk:
            chunks.append(" ".join(current_chunk))
            
            # Retain words from the end of the current chunk for overlap
            overlap_chunk = []
            overlap_len = 0
            for w in reversed(current_chunk):
                if overlap_len + len(w) + 1 <= overlap:
                    overlap_chunk.insert(0, w)
                    overlap_len += len(w) + 1
                else:
                    break
            
            current_chunk = overlap_chunk
            current_length = overlap_len

        current_chunk.append(word)
        current_length += len(word) + 1

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks
