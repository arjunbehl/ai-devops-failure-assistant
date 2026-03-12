# from skills import analyze_log_file, search_docs, create_ticket

# class DevOpsAgent:
#     def __init__(self):
#         self.skills = {
#             "analyze_logs": analyze_log_file,
#             "search_docs": search_docs,
#             "create_ticket": create_ticket
#         }

#     def run(self, task, *args):
#         if task in self.skills:
#             return self.skills[task](*args)
#         else:
#             return f"Unknown task: {task}"

# if __name__ == "__main__":

#     agent = DevOpsAgent()

#     # Example 1: Analyze log
#     result = agent.run("analyze_logs", "dependency_error.log")
#     print("Analysis Result:", result)

#     # Example 2: Search docs
#     res = agent.run("search_docs", "docker pull error")
#     print(res)

#     # Example 3: Create ticket
#     ticket = agent.run("create_ticket", "Dependency Issue", "Upgrade react package")
#     print(ticket)

from agent.skills import analyze_log_file

class DevOpsAgent:
    def __init__(self):
        self.skills = {
            "analyze_logs": analyze_log_file
        }

    def run(self, task, *args):
        if task in self.skills:
            return self.skills[task](*args)
        return f"Unknown task: {task}"

if __name__ == "__main__":
    agent = DevOpsAgent()
    logs = "data/logs/test_failure.log"
    result = agent.run("analyze_logs", logs)
    print(result)