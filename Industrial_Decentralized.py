import random
import math
import time

# ==============================
# CONFIGURATION
# ==============================
NUM_ROBOTS = 20
NUM_TASKS = 8
PLANT_SIZE = 120
MAX_SPEED = 2.0
SAFE_DIST = 3.0
FAILURE_PROB = 0.05

CYCLE_DELAY = 2.5        # very slow cycle
STEP_DELAY = 1.5         # delay between decisions

# ==============================
# ROBOT
# ==============================
class Robot:
    def __init__(self, rid):
        self.id = rid
        self.x = random.uniform(0, PLANT_SIZE)
        self.y = random.uniform(0, PLANT_SIZE)
        self.vx = 0
        self.vy = 0
        self.task = None
        self.load = 0
        self.failed = False

    def dist(self, x, y):
        return math.hypot(self.x - x, self.y - y)

# ==============================
# TASK
# ==============================
class Task:
    def __init__(self, tid):
        self.id = tid
        self.x = random.uniform(10, PLANT_SIZE - 10)
        self.y = random.uniform(10, PLANT_SIZE - 10)
        self.priority = random.randint(1, 5)
        self.owner = None
        self.done = False

# ==============================
# DECENTRALIZED TASK CLAIM
# ==============================
def task_claim(robot, tasks):
    if robot.failed or robot.task is not None:
        return

    free_tasks = [t for t in tasks if not t.done and t.owner is None]
    if not free_tasks:
        return

    chosen = min(
        free_tasks,
        key=lambda t: robot.dist(t.x, t.y) - t.priority * 2
    )

    chosen.owner = robot.id
    robot.task = chosen
    robot.load += chosen.priority

    print(f"🤖 Robot {robot.id:02d} evaluated surroundings")
    time.sleep(STEP_DELAY)

    print(f"📌 Robot {robot.id:02d} selected Task {chosen.id} "
          f"(priority {chosen.priority})")
    time.sleep(STEP_DELAY)

# ==============================
# FAILURE INJECTION
# ==============================
def induce_failure(robot):
    if robot.failed or robot.task is None:
        return False
    if random.random() < FAILURE_PROB:
        robot.failed = True
        return True
    return False

# ==============================
# STEPWISE FAILURE HANDLING
# ==============================
def collaborative_recovery(failed_robot, robots):
    lost_task = failed_robot.task
    print(f"\n⚠️  FAILURE CONFIRMED")
    print(f"❌ Robot {failed_robot.id:02d} stopped while executing Task {lost_task.id}")
    time.sleep(STEP_DELAY)

    print("🔍 Swarm searching for available robots...")
    time.sleep(STEP_DELAY)

    available = []
    for r in robots:
        if not r.failed and r.task is None:
            print(f"   ↳ Robot {r.id:02d} is AVAILABLE")
            available.append(r)
            time.sleep(0.7)

    if not available:
        print("⏸️  No robot currently available for reassignment")
        lost_task.owner = None
        failed_robot.task = None
        return

    print("\n📊 Evaluating best replacement based on distance & load...")
    time.sleep(STEP_DELAY)

    helper = min(
        available,
        key=lambda r: r.dist(lost_task.x, lost_task.y) + r.load
    )

    print(f"🤝 Robot {helper.id:02d} accepted Task {lost_task.id}")
    time.sleep(STEP_DELAY)

    helper.task = lost_task
    helper.load += lost_task.priority
    lost_task.owner = helper.id
    failed_robot.task = None

# ==============================
# MOTION & EXECUTION
# ==============================
def execute_task(robot):
    if robot.failed or robot.task is None:
        return

    dx = robot.task.x - robot.x
    dy = robot.task.y - robot.y

    robot.vx += dx * 0.03
    robot.vy += dy * 0.03

    speed = math.hypot(robot.vx, robot.vy)
    if speed > MAX_SPEED:
        robot.vx = (robot.vx / speed) * MAX_SPEED
        robot.vy = (robot.vy / speed) * MAX_SPEED

    robot.x += robot.vx
    robot.y += robot.vy

    if math.hypot(dx, dy) < 2:
        print(f"✅ Robot {robot.id:02d} completed Task {robot.task.id}")
        robot.task.done = True
        robot.task = None
        time.sleep(STEP_DELAY)

# ==============================
# DASHBOARD (VERY CLEAN)
# ==============================
def dashboard(step, robots):
    print(f"\n🏭 COLLABORATIVE DECISION CYCLE {step}")
    print("-" * 70)
    for r in robots:
        if r.failed:
            state = "FAILED"
        elif r.task:
            state = f"TASK-{r.task.id}"
        else:
            state = "IDLE"

        print(f"Robot {r.id:02d} | Pos({r.x:6.1f},{r.y:6.1f}) | Load {r.load:2d} | {state}")

# ==============================
# MAIN LOOP
# ==============================
robots = [Robot(i) for i in range(NUM_ROBOTS)]
tasks = [Task(i) for i in range(NUM_TASKS)]

for step in range(50):
    dashboard(step, robots)
    time.sleep(CYCLE_DELAY)

    for r in robots:
        task_claim(r, tasks)

    for r in robots:
        if induce_failure(r):
            collaborative_recovery(r, robots)

    for r in robots:
        execute_task(r)
