import random
import time

class ServiceInstance:
    def __init__(self, service_id, instance_id, host, port):
        self.service_id = service_id
        self.instance_id = instance_id
        self.host = host
        self.port = port

    def __repr__(self):
        return f"{self.service_id}@{self.host}:{self.port} (ID: {self.instance_id})"

class RoundRobinLoadBalancer:
    def __init__(self, instances):
        self.instances = instances
        self.index = 0

    def choose(self):
        if not self.instances:
            return None
        instance = self.instances[self.index]
        self.index = (self.index + 1) % len(self.instances)
        return instance

class RandomLoadBalancer:
    def __init__(self, instances):
        self.instances = instances

    def choose(self):
        if not self.instances:
            return None
        return random.choice(self.instances)

def simulate_load_balancing():
    print("=" * 70)
    print("     SIMULATION: SPRING CLOUD RANDOM LOAD BALANCER CONFIGURATION")
    print("=" * 70)
    
    # Define product-service instances running on different ports
    instances = [
        ServiceInstance("product-service", "prod-inst-1", "127.0.0.1", 8081),
        ServiceInstance("product-service", "prod-inst-2", "127.0.0.1", 8082)
    ]
    
    print("Registered Instances for 'product-service':")
    for inst in instances:
        print(f" - {inst}")
    print("-" * 70)

    # 1. Default Round Robin Simulation
    print("\n[Strategy 1] Default Round Robin Load Balancer (Equal division)")
    rr_lb = RoundRobinLoadBalancer(instances)
    rr_results = []
    for i in range(1, 11):
        selected = rr_lb.choose()
        rr_results.append(selected.port)
        print(f"Request #{i:02d} -> Routed to: {selected}")
        time.sleep(0.05)
    
    # Calculate stats
    port_counts_rr = {8081: rr_results.count(8081), 8082: rr_results.count(8082)}
    print(f"-> Round Robin distribution: Port 8081: {port_counts_rr[8081]} requests, Port 8082: {port_counts_rr[8082]} requests")

    # 2. Random Load Balancer Simulation
    print("\n[Strategy 2] Configured Random Load Balancer (SPRING-CLOUD-S05-EX03)")
    random_lb = RandomLoadBalancer(instances)
    random_results = []
    for i in range(1, 11):
        selected = random_lb.choose()
        random_results.append(selected.port)
        print(f"Request #{i:02d} -> Routed to: {selected}")
        time.sleep(0.05)

    # Calculate stats
    port_counts_rand = {8081: random_results.count(8081), 8082: random_results.count(8082)}
    print(f"-> Random distribution: Port 8081: {port_counts_rand[8081]} requests, Port 8082: {port_counts_rand[8082]} requests")
    print("=" * 70)
    print("Notice how Random distributes requests unpredictably, helping resolve uneven server load problems.")
    print("=" * 70)

if __name__ == '__main__':
    simulate_load_balancing()