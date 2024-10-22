#[Fait avec l'aide de Chat GPT]Supervision (5 points)
class Disk:
    def __init__(self, total: float, used: float):
        self.total = total
        self.used = used

    @property
    def free(self) -> float:
        return self.total - self.used

    @property
    def used_perc(self) -> float:
        return self.used / self.total if self.total > 0 else 0

    def __repr__(self) -> str:
        return f"Disk[total: {self.total} Gb, used: {self.used} Gb]"

    def __lt__(self, other):
        if isinstance(other, Disk):
            return self.used_perc < other.used_perc
        return NotImplemented

# Exemple d'utilisation
disk1 = Disk(total=10, used=2)
disk2 = Disk(total=20, used=5)

print(disk1.free)  # 8
print(disk2.free)  # 15
print(disk1.used_perc)  # 0.2
print(disk2.used_perc)  # 0.25

disks = [disk1, disk2]
disks_sorted = sorted(disks)

for disk in disks_sorted:
    print(disk)
