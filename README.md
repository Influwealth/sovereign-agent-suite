# Sovereign Agent Suite

Agent registry and lifecycle manager for the Sovereign Automation System.

## Role
Central registry for all SAP-compliant agents:
- Agent registration and discovery
- Lifecycle management (start, stop, restart, health)
- Capability index for DeepFlex routing
- Agent version management

## Port: 7790

## Agent Types Managed
| Agent | Node | Capabilities |
|-------|------|-------------|
| argus-prime | argus-prime | device, capsule, infra |
| deepflex-supervisor | sovereign-stack | orchestration, routing |
| wealthbridge-os | sovereign-stack | business, finance |
| qre-caffeine | qre-agent-platform | prediction, icp |
| token-gateway | sovereign-stack | token, bridge |
| nvidia-scheduler | nvidia-resource-suite | gpu, compute |

## SAP Integration
Node ID: `sovereign-agent-suite`
