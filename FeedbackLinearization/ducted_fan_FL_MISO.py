# Ducted Fan Feedback Linearization
# Dynamic Model: https://pdf.sciencedirectassets.com/271426/1-s2.0-S0005109800X00854/1-s2.0-S0005109801001492/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFEaCXVzLWVhc3QtMSJGMEQCICm0A%2Fu33OHOe7xg1ChEuharNTPPneu8zHHXONpeBbdfAiAMMPv9MB7SxGri8JLiBlKD9vBcB0sr1YU9c8jC9KN6%2FCqzBQh6EAUaDDA1OTAwMzU0Njg2NSIMA1SuGllFiXJSCfQEKpAFV5ydA%2FZGALxhReZWskhs7bSmfNZy9iJu3m1v4d1aCXFqX5wB9wajTgOjD3%2B3AG%2BVECGYpiHv4t0OZWbz8QVqdveUCi4ojxQy6ax9vJSXUwjEA2xYbjU74A5UlgGwPvTdVM%2FvlsJLU5qUZQ75BI9KHCLBPBhBja1JSk9N0fHTuGd4M1rXi%2FClXCP7EtWtz2iyKSR72DmePQQDIKUQMl%2Br1N7RrUeleUKI11asukiaxePl553oOHXPkeczzsDiVSOZwwDx8qgVMXbNjO%2BY6qaPsrm5vKHQlIk0b7jawd4A0%2FNowuvPXq%2FyHyZUKIAKYmzEk4%2FKnMFI%2F%2FVHTkc0lEtMpGb%2FxLIsQcyTouXNLSRIrbeSZ7Tz7THK5b0Cmr4iqhRSuPW5eqadNG%2F4S%2Fuj0DPpG7x%2BDvlmCJWolLiUr8crqKemLwki66p8KtRyI7Duobp6wql%2BULuid%2FQ7bvonQSZKx1LmfTOsGNsQEWsBs4gFtqY4jeGr3h4dtqv5L91o7Obqdo4%2BfWUEYcjrnKAvZOv8aCBwzI2HO55oWwexIX9ED8HI%2FxG3U57BjkjmnKZ1BuMBQt98sTLUnq4rMsVi50wEXSw8RV8hxqDLrThsFyJaQ1wk0c5HUDytIg0AO72pVdG4TAAdDZanOrXrb3I2l%2Bnk3Bo90WWXcXsK3n%2B3mVqlp6guOKb0G7yu0QIcU9jKabApSyvV26X0F%2FLQucgtItWqYQK%2FM5qEvg6iV59kDVCDCEzP2%2B68kz9rw8laX9s1jorSzliKii37RAuPmnFeiurSx5Ewg%2Bv17puCzjqsVbEBUOITco1CIZDiYcgVIf%2B57hCu%2BQ86dPNvplmfgnSmN1wok58AcYaE896ndz5%2FIC3fdcswsYq2sAY6sgFtlaui5S9ALf4WlerOOJf0WJUabLXcH4VNm1aa3PyX3v1KytsR0U%2FhJrwPDv%2Be3sxEU3OTz7VCelGuh3TODz8IwJ5n4FR2zGS3mFOPDsVjL6h3Q%2FUbC5m5QeHGbuSAYctBV7Z4JYNqaa19HDj6sI1EiQTnaZtZ%2FwGzgf2oHAg1s20xyIJs%2FFimxeGQN9Qx8ekv6oMa6ZyxAP1sbW5k8KGbu0yP3Qu86fg7NA7C7Hl0j9nZ&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240403T175153Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTYSTN3WCJP%2F20240403%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=3f5b9ee3d8a559e9f42ab7958b4111e7cc111c24f14719d3507f9510fbf0d6f7&hash=f328bbf616b35364c7e39ea8c7e7b26b9677d06a72245bccb77371062f27c05d&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S0005109801001492&tid=spdf-51a44b9d-dd7c-4ef0-a495-8a5bf59bafdf&sid=472b2d774fcd1742c65a7879a13ca33e7badgxrqb&type=client&tsoh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&ua=0f135851050f0b5a0559&rr=86eae8c72ac17cea&cc=us
import sympy as sym
from feedback_linearization import FeedbackLinearization

x, xdot, y, ydot, theta, thetadot = sym.symbols('x, xdot, y, ydot, theta, thetadot')
J = 0.13
r = .358
m = 8.5
g = 9.8
n = 6

states = sym.Matrix([x, xdot, y, ydot, theta, thetadot])

f = sym.Matrix([xdot, -g*sym.sin(theta), ydot, m*g*(sym.cos(theta) - 1), thetadot, 0])
g_v = sym.Matrix([0, sym.cos(theta)/m, 0, sym.sin(theta)/m, 0, r/J])

input_linearizer = FeedbackLinearization(f, g_v, n, states)

linearizable_bool = input_linearizer.input_state_linearizable_check()
print(linearizable_bool)


