# Agent Task

Source PDF: `(2.138)--【第42节】课后作业解析.pdf`
Chapter count: 1

## Work Order

1. Read `queue.json`.
2. Process `chapters/*.md` in ascending `order`.
3. Keep image links pointing to `../images/...`.
4. Write your final office-processing output wherever the user requested.

## Useful Commands

```bash
python3 "/Users/devilrecal/Downloads/教材/信号与系统/116 (2.138)--【第42节】课后作业解析/tools/agent_queue.py" list "/Users/devilrecal/Downloads/教材/信号与系统/116 (2.138)--【第42节】课后作业解析"
python3 "/Users/devilrecal/Downloads/教材/信号与系统/116 (2.138)--【第42节】课后作业解析/tools/agent_queue.py" mark "/Users/devilrecal/Downloads/教材/信号与系统/116 (2.138)--【第42节】课后作业解析" 1 processing
python3 "/Users/devilrecal/Downloads/教材/信号与系统/116 (2.138)--【第42节】课后作业解析/tools/agent_queue.py" mark "/Users/devilrecal/Downloads/教材/信号与系统/116 (2.138)--【第42节】课后作业解析" 1 done
python3 "/Users/devilrecal/Downloads/教材/信号与系统/116 (2.138)--【第42节】课后作业解析/tools/agent_queue.py" validate "/Users/devilrecal/Downloads/教材/信号与系统/116 (2.138)--【第42节】课后作业解析"
```
