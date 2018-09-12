import sublime
import sublime_plugin
import time


class Watcher(sublime_plugin.EventListener):
	def on_load(self, view):
		win_inst = view.window()
		status_str=' FILE: '+str(view.file_name())+' SIZE: '+str(view.size())
		win_inst.status_message(status_str)
		log_file="C:\\Users\\coder\\Desktop\\sublime.log"
		with open(log_file, 'a') as logstream:
			logstream.write(time.asctime()+"\t"+self.view.file_name()+'\n')
		logstream.close()
