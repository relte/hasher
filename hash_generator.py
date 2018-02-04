import hashlib

def get_file_hash(file_path: str, algorithm: str) -> str:
    hasher = getattr(hashlib, algorithm)()
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()
