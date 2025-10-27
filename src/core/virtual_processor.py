class VirtualProcessor:
    def __init__(self, name):
        self.name = name
        self.registers = [0] * 10
        self.memory = {}
        self.virtual_time = 0  # Виртуальные "такт. циклы"
        self.last_cmp = False

    def process_instruction(self, instr):
        op = instr['op']
        args = instr.get('args', [])

        # Моделируем стоимость операций
        if op == "MUL":
            self.virtual_time += 10
        elif op == "ADD":
            self.virtual_time += 1
        elif op == "LOAD":
            self.virtual_time += 2
        elif op == "STORE":
            self.virtual_time += 2
        else:
            self.virtual_time += 1

        if op == "SET":
            self.registers[args[0]] = args[1]
        elif op == "ADD":
            self.registers[args[0]] = self.registers[args[1]] + self.registers[args[2]]
        elif op == "MUL":
            self.registers[args[0]] = self.registers[args[1]] * self.registers[args[2]]
        elif op == "LOAD":
            self.registers[args[0]] = self.memory.get(args[1], 0)
        elif op == "STORE":
            self.memory[args[1]] = self.registers[args[0]]
        elif op == "INPUT":
            self.registers[args[0]] = int(input(f"[{self.name}] INPUT: "))
        elif op == "PRINT":
            print(f"[{self.name}] PRINT: {self.registers[args[0]]}")
        elif op == "CMP":
            self.last_cmp = self.registers[args[0]] == self.registers[args[1]]
        elif op == "JMP_IF":
            if self.last_cmp:
                return args[0]
        return None

    def execute(self, instructions):
        import time
        self.virtual_time = 0
        real_start = time.time()
        i = 0
        while i < len(instructions):
            jump = self.process_instruction(instructions[i])
            if jump is not None:
                i = jump
            else:
                i += 1
        real_end = time.time()
        print(f"[{self.name}] Реальное время: {real_end-real_start:.3f} сек")
        print(f"[{self.name}] Виртуальное время: {self.virtual_time} тактов")
