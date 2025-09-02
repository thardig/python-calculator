import tkinter as tk
import ast
import operator as op

# ----- Safe evaluator -----
_ALLOWED_BIN_OPS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Mod: op.mod,
    ast.Pow: op.pow,
}
_ALLOWED_UNARY_OPS = {
    ast.UAdd: op.pos,
    ast.USub: op.neg,
}

def _eval_ast(node):
    if isinstance(node, ast.Expression):
        return _eval_ast(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.Num):
        return node.n
    if isinstance(node, ast.UnaryOp) and type(node.op) in _ALLOWED_UNARY_OPS:
        return _ALLOWED_UNARY_OPS[type(node.op)](_eval_ast(node.operand))
    if isinstance(node, ast.BinOp) and type(node.op) in _ALLOWED_BIN_OPS:
        left = _eval_ast(node.left)
        right = _eval_ast(node.right)
        return _ALLOWED_BIN_OPS[type(node.op)](left, right)
    raise ValueError("Unsupported expression")

def safe_eval(expr: str):
    allowed_chars = "0123456789.+-*/()% "
    if any(ch not in allowed_chars for ch in expr):
        raise ValueError("Invalid character")
    tree = ast.parse(expr, mode="eval")
    return _eval_ast(tree)


# ----- Calculator GUI -----
class Calculator(tk.Frame):
    def __init__(self, master):
        super().__init__(master, padx=15, pady=15)
        self.master.title("Python Calculator")
        self.master.resizable(False, False)

        self.var = tk.StringVar(value="")

        # Display
        self.entry = tk.Entry(
            self, textvariable=self.var, justify="right",
            font=("Segoe UI", 18), bd=8, relief="sunken"
        )
        self.entry.grid(row=0, column=0, columnspan=5, sticky="nsew", ipady=10)
        self.entry.focus_set()

        # Button layout
        buttons = [
            ["7", "8", "9", "/", "⌫"],
            ["4", "5", "6", "*", "C"],
            ["1", "2", "3", "-", "("],
            [".", "0", "=", "+", ")"],
        ]

        for r, row in enumerate(buttons, start=1):
            for c, label in enumerate(row):
                self.make_button(label, r, c)

        # Grid stretch
        for i in range(5):
            self.columnconfigure(i, weight=1)
        for i in range(5):
            self.rowconfigure(i, weight=1)

        # Keyboard bindings
        self.master.bind("<Return>", lambda e: self.evaluate())
        self.master.bind("<KP_Enter>", lambda e: self.evaluate())
        self.master.bind("<BackSpace>", lambda e: self.backspace())
        self.master.bind("<Escape>", lambda e: self.clear())
        for ch in "0123456789+-*/().%":
            self.master.bind(ch, self.type_char)

        self.pack(fill="both", expand=True)

    # ----- Button creation -----
    def make_button(self, label, r, c):
        # Numbers → dark gray, Operators → orange
        if label.isdigit() or label == ".":
            bg, fg = "#333333", "white"
        else:
            bg, fg = "#ff6600", "white"

        btn = tk.Button(
            self, text=label, width=5, height=2,
            bg=bg, fg=fg, font=("Segoe UI", 14, "bold"),
            relief="raised", bd=3,
            command=lambda l=label: self.on_button(l)
        )
        btn.grid(row=r, column=c, padx=4, pady=4, sticky="nsew")

    # ----- Actions -----
    def on_button(self, label: str):
        if label == "C":
            self.clear()
        elif label == "⌫":
            self.backspace()
        elif label == "=":
            self.evaluate()
        else:
            self.append(label)

    def type_char(self, event):
        self.append(event.char)

    def append(self, text: str):
        self.entry.insert(tk.END, text)

    def clear(self):
        self.var.set("")

    def backspace(self):
        current = self.var.get()
        if current:
            self.var.set(current[:-1])

    def evaluate(self):
        expr = self.var.get().strip()
        if not expr:
            return
        try:
            result = safe_eval(expr)
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self.var.set(str(result))
        except Exception:
            self.var.set("Error")


if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
