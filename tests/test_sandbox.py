from app.sandbox.sandbox_service import SandboxService

result = SandboxService.execute("sample_repo")

print("\n========== TEST RESULT ==========")
print("Success :", result.success)

print("\nOutput:")
print(result.output)

print("\nErrors:")
print(result.errors)