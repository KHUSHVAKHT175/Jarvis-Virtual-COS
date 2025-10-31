class UserInterface:
    def __init__(self, log_ref=None):
        self.log_ref = log_ref

    def get_command(self):
        try:
            cmd = input(">>> ").strip()
            if cmd:
                return cmd
            return None
        except (EOFError, KeyboardInterrupt):
            return None

    def process(self, cmd, memory):
        memory.add(cmd)
        answer = f"Выполнена команда: {cmd}"
        if self.log_ref is not None:
            self.log_ref.append(f">>> {cmd}")
            self.log_ref.append(answer)
        return answer

    def respond(self, message):
        print(message)
        if self.log_ref is not None:
            self.log_ref.append(message)
