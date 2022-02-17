import sublime
import sublime_plugin


class SendCurrentToTerminusCommand(sublime_plugin.TextCommand):
    """
    Send current line to terminus for execution and advance cursor to end of next line
    """
    def run(self, edit, tag=None, visible_only=False):
        self.view.window().run_command("terminus_send_string", {
            "string": self.view.substr(self.view.line(self.view.sel()[0])) + '\n',
            "tag": tag,
            "visible_only": visible_only
            })
        self.view.run_command("move", {"by": "lines", "forward": True})
