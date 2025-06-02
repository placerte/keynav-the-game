from kivy.uix.button import Button as kivy_Button
from typing import Callable, Any

class Button(kivy_Button):
    def bind(
        self,
        *,
        text: Callable[[kivy_Button, str], None] = None,
        on_press: Callable[[kivy_Button], None] = None,
        **kwargs: Callable[..., Any]
    ) -> "Button":
        if text:
            super().bind(text=text)
        if on_press:
            super().bind(on_press=on_press)
        if kwargs:
            super().bind(**kwargs)
        return self
