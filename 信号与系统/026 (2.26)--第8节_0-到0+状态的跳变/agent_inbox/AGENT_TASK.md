# Agent Task

Source PDF: `(2.26)--第8节_0-到0+状态的跳变.pdf`
Chapter count: 1

## Work Order

1. Read `queue.json`.
2. Process `chapters/*.md` in ascending `order`.
3. Keep image links pointing to `../images/...`.
4. Write your final office-processing output wherever the user requested.

## Useful Commands

```bash
python3 "/Users/devilrecal/Downloads/教材/信号与系统/026 (2.26)--第8节_0-到0+状态的跳变/tools/agent_queue.py" list "/Users/devilrecal/Downloads/教材/信号与系统/026 (2.26)--第8节_0-到0+状态的跳变"
python3 "/Users/devilrecal/Downloads/教材/信号与系统/026 (2.26)--第8节_0-到0+状态的跳变/tools/agent_queue.py" mark "/Users/devilrecal/Downloads/教材/信号与系统/026 (2.26)--第8节_0-到0+状态的跳变" 1 processing
python3 "/Users/devilrecal/Downloads/教材/信号与系统/026 (2.26)--第8节_0-到0+状态的跳变/tools/agent_queue.py" mark "/Users/devilrecal/Downloads/教材/信号与系统/026 (2.26)--第8节_0-到0+状态的跳变" 1 done
python3 "/Users/devilrecal/Downloads/教材/信号与系统/026 (2.26)--第8节_0-到0+状态的跳变/tools/agent_queue.py" validate "/Users/devilrecal/Downloads/教材/信号与系统/026 (2.26)--第8节_0-到0+状态的跳变"
```
