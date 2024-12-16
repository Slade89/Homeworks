def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()

#inner_function() Вызвать не удается, так как функция находится вне своей области видимости