class HiddenMessage:
    def __init__(self, visible_part, hidden_part):
        self.visible_part = visible_part
        self.hidden_part = hidden_part

    def show_partial(self):
        print(f"{self.visible_part} {'_' * len(self.hidden_part)}")

    def prompt_for_reveal(self):
        user_input = input("Type the missing word to reveal the message: ").strip()
        while user_input.lower() != self.hidden_part.lower():
            print("Nope.")
            user_input = input("Type the missing word to reveal the message: ").strip()
        self.reveal_message()

    def reveal_message(self):
        full_message = f"{self.visible_part} {self.hidden_part}"
        print(f"\n{full_message}")


def main():
    message = HiddenMessage("Hello", "world")
    message.show_partial()
    message.prompt_for_reveal()

if __name__ == "__main__":
    main()
