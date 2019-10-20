from typing import Sequence, Union
import abc
import collections
import dataclasses as dc


@dc.dataclass
class Notifier(abc.ABC):

    recipient: Union[str, Sequence[str]]
    sender: str = dc.field(default=None)

    def __post_init(self):
        if self._seq_but_not_str(self.recipient):
            return
        self.recipient = tuple([self.recipient])

    def _seq_but_not_str(self, obj):
        return isinstance(obj, collections.abc.Sequence) and not isinstance(
            obj, (str, bytes, bytearray)
        )

    @abc.abstractmethod
    def notify(self, message):
        """Send the notification."""


class SMSNotifier(Notifier):
    def notify(self, message):
        raise NotImplementedError
