def test_function():
        def inner_function():
           d = print(f"Я в области видимости функции")
        inner_function()
function = inner_function()
print(function)
