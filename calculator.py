import wx

class CalculatorFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Calculator", size=(300, 400))

        panel = wx.Panel(self)

        self.display = wx.TextCtrl(panel, style=wx.TE_RIGHT)

        grid = wx.GridSizer(4, 4, 10, 10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        for label in buttons:
            button = wx.Button(panel, label=label)
            grid.Add(button, 1, wx.EXPAND)
            button.Bind(wx.EVT_BUTTON, self.on_button_click)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.display, 1, wx.EXPAND | wx.ALL, 10)
        vbox.Add(grid, 3, wx.EXPAND | wx.ALL, 10)

        panel.SetSizer(vbox)

        self.Centre()

    def on_button_click(self, event):
        label = event.GetEventObject().GetLabel()
        current_value = self.display.GetValue()

        if label == '=':
            try:
                result = str(eval(current_value))
                self.display.SetValue(result)
            except Exception as e:
                self.display.SetValue("Error")
        else:
            self.display.SetValue(current_value + label)


class CalculatorApp(wx.App):
    def OnInit(self):
        frame = CalculatorFrame()
        frame.Show()
        return True

app = CalculatorApp()
app.MainLoop()