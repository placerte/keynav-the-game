from kivy.uix.button import Button as KiviBytton
from typing import Callable, Any


class Button(KiviBytton):

    def bind(
        self,
        *,
        text: Callable[[KiviBytton, str], None] = None,
        on_press: Callable[[KiviBytton], None] = None,
        size: Callable[[KiviBytton], None] = None,
        **kwargs: Callable[..., Any]
    ) -> "Button":
        if text:
            super().bind(text=text)
        if on_press:
            super().bind(on_press=on_press)
        if size:
            super().bind(size=size)
        if kwargs:
            super().bind(**kwargs)
        return self
