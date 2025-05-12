class FlagManager:
    def __init__(self):
        self.flags = []

    def add_flag(self, flag):

            if isinstance(flag, list):
                for fla in flag:
                    if not fla in self.flags:
                        self.flags.append(fla)
            elif isinstance(flag, str):
                if not flag in self.flags:
                    self.flags.append(flag)

    def check_flag(self, flag):
        return flag in self.flags

    def del_flag(self, flag):
        for fla in self.flags:
            if fla == flag:
                self.flags.remove(fla)