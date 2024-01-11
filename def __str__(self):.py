def __str__(self):
    if self.is_empty():
        return "[]"
    else:
        products_str = ", ".join([str(p) for p in self._products])
        return f"[{products_str}]"