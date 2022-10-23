# CI Info

Get details about the current Continuous Integration environment. Inspired by https://github.com/watson/ci-info.

## Example

```python
import ci_info

print(ci_info.is_ci()) # True
print(ci_info.get())  # CIInfo(name='GitHub Actions', is_ci=True, is_pr=False)
```
