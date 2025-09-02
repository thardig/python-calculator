🖩 Python GUI Calculator

- A clean and simple calculator built with Python Tkinter.

- Dark gray number buttons and bright orange operator buttons 🎨

- Keyboard support (type directly, use Enter/Backspace/Escape) ⌨️

- Safe expression evaluation using Python’s ast module ✅

- Supports parentheses, decimals, powers, and modulus

🚀 Features

- GUI built with Tkinter (no extra installs needed)

- Safe math parsing (no eval, prevents unsafe code execution)

- Keyboard shortcuts

- - Enter / Numpad Enter → =

- - Backspace → ⌫

- - Escape → Clear

- - Operators supported: + - * / % ** ( )

📸 Screenshot

![Calculator Screenshot](screenshot.png)

⚡ Installation & Run

Clone the repo:

git clone https://github.com/YOUR-USERNAME/python-calculator.git
cd python-calculator


Run the program:

python calculator.py


✅ Works out of the box (Tkinter is included with Python on Windows & macOS).

🛠️ Project Structure
python-calculator/
│── calculator.py   # Main application
│── README.md       # Project documentation
└── screenshot.png  # (Optional) Example UI image

📚 How It Works

Tkinter manages the window, buttons, and layout.

AST (Abstract Syntax Tree) parses math expressions safely.

Button grid is created dynamically for digits and operators.

Custom colors distinguish numbers (dark gray) and operators (orange).

🔮 Future Improvements

Dark mode toggle 🌙

Calculation history panel 📜

Memory buttons (M+, M-, MR, MC) 💾

Hover effects for modern UI ✨

👨‍💻 Author

Made with ❤️ in Python by Trevor Hardig
