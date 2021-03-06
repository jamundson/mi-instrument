from mi.core.instrument.instrument_driver import SingleConnectionInstrumentDriver
from mi.instrument.teledyne.workhorse.driver import WorkhorseProtocol, WorkhorsePrompt, NEWLINE
# do not remove, facilitates playback
from mi.instrument.teledyne.workhorse.driver import create_playback_protocol


class InstrumentDriver(SingleConnectionInstrumentDriver):
    """
    Specialization for this version of the workhorse ADCP driver
    """

    def _build_protocol(self):
        """
        Construct the driver protocol state machine.
        """
        self._protocol = WorkhorseProtocol(WorkhorsePrompt, NEWLINE, self._driver_event)
