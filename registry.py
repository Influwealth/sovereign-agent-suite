"""
Sovereign Agent Suite — Agent Registry and Lifecycle Manager
Sovereign Agent Protocol node: sovereign-agent-suite
Port: 7790
"""
from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class AgentStatus(str, Enum):
    REGISTERED = "registered"
    ONLINE = "online"
    OFFLINE = "offline"
    ERROR = "error"


@dataclass
class AgentRegistration:
    agent_id: str
    node_id: str
    capabilities: list[str]
    base_url: str
    port: int
    language: str
    status: AgentStatus = AgentStatus.REGISTERED
    version: str = "1.0.0"
    registration_id: str = field(default_factory=lambda: str(uuid.uuid4()))


class SovereignAgentRegistry:
    def __init__(self) -> None:
        self.agents: dict[str, AgentRegistration] = {}
        self._seed_known_agents()

    def _seed_known_agents(self) -> None:
        known = [
            AgentRegistration("argus-prime", "argus-prime", ["device", "capsule", "infra", "agent"], "http://localhost:7700", 7700, "python"),
            AgentRegistration("deepflex-supervisor", "deepflex-supervisor", ["orchestration", "routing", "dispatch"], "http://localhost:8000", 8000, "typescript"),
            AgentRegistration("wealthbridge-os", "wealthbridge-os", ["business", "finance", "invoice", "cashflow"], "http://localhost:8001", 8001, "typescript"),
            AgentRegistration("qre-caffeine", "qre-caffeine-agent", ["prediction", "icp", "quantum"], "http://localhost:7750", 7750, "motoko+typescript"),
            AgentRegistration("token-gateway", "token-gateway", ["token", "bridge", "transfer"], "http://localhost:8002", 8002, "typescript"),
        ]
        for agent in known:
            self.agents[agent.agent_id] = agent

    def register(self, agent_id: str, node_id: str, capabilities: list[str], base_url: str, port: int, language: str) -> AgentRegistration:
        reg = AgentRegistration(agent_id, node_id, capabilities, base_url, port, language)
        self.agents[agent_id] = reg
        return reg

    def find_by_capability(self, capability: str) -> list[AgentRegistration]:
        return [a for a in self.agents.values() if any(capability in cap for cap in a.capabilities)]

    def status(self) -> dict[str, Any]:
        return {"total": len(self.agents), "online": sum(1 for a in self.agents.values() if a.status == AgentStatus.ONLINE), "agents": {k: v.status for k, v in self.agents.items()}}


if __name__ == "__main__":
    registry = SovereignAgentRegistry()
    print(f"Registered {len(registry.agents)} agents")
    finance_agents = registry.find_by_capability("finance")
    print(f"Finance-capable agents: {[a.agent_id for a in finance_agents]}")
