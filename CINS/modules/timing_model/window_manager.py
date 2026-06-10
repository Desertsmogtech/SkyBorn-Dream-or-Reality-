"""
CINS.modules.timing_model.window_manager
-----------------------------------------
Maintains the registry of active timing windows assigned by TimingModel.

Windows are keyed by task_id and stored in insertion order.
"""


class WindowManager:
    """
    In-memory store for active timing windows.
    """

    def __init__(self):
        self._windows: dict = {}

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def register(self, window: dict) -> None:
        """
        Add a timing window to the active registry.

        Parameters
        ----------
        window : dict
            Must contain "task_id".  Typically the dict returned by
            TimingModel.assign_window().
        """
        task_id = window.get("task_id")
        if task_id is None:
            raise ValueError("Window dict must contain a 'task_id' key.")
        self._windows[task_id] = window

    def lookup(self, task_id: str):
        """
        Retrieve the window for *task_id*, or None if not registered.
        """
        return self._windows.get(task_id)

    def remove(self, task_id: str) -> None:
        """
        Deregister a window.  Silently ignores unknown task_ids.
        """
        self._windows.pop(task_id, None)

    def active(self) -> list:
        """
        Returns
        -------
        list of all currently registered window dicts.
        """
        return list(self._windows.values())

    def count(self) -> int:
        """
        Returns
        -------
        int -- number of currently active windows.
        """
        return len(self._windows)
