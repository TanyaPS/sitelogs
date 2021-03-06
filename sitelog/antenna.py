import re

from sitelog.sections import (
    SubSection,
    SectionList,
)
from sitelog import _format_string
from datetime import datetime as dt


class AntennaType(SubSection):
    def __init__(
        self,
        antenna_type="",
        serial_number="",
        antenna_reference="",
        up="",
        north="",
        east="",
        north_alignment="",
        radome_type="",
        radome_serial="",
        cable_type="",
        cable_length="",
        date_installed="",
        date_removed="",
        additional="",
    ):
        super().__init__()
        self._data = self._template_dict()
        self.antenna_type = antenna_type
        self.serial_number = serial_number
        self.antenna_reference = antenna_reference
        self.up = up
        self.north = north
        self.east = east
        self.north_alignment = north_alignment
        self.radome_type = radome_type
        self.radome_serial = radome_serial
        self.cable_type = cable_type
        self.cable_length = cable_length
        self.date_installed = date_installed
        self.date_removed = date_removed
        self.additional = additional

    def _template_dict(self):
        data = {
            "Antenna Type": "(A20, from rcvr_ant.tab; see instructions)",
            "Serial Number": "(A*, but note the first A5 is used in SINEX)",
            "Antenna Reference Point": '(BPA/BCR/XXX from "antenna.gra"; see instr.)',
            "Marker->ARP Up Ecc. (m)": "(F8.4)",
            "Marker->ARP North Ecc(m)": "(F8.4)",
            "Marker->ARP East Ecc(m)": "(F8.4)",
            "Alignment from True N": "(deg; + is clockwise/east)",
            "Antenna Radome Type": "(A4 from rcvr_ant.tab; see instructions)",
            "Radome Serial Number": "",
            "Antenna Cable Type": "(vendor & type number)",
            "Antenna Cable Length": "(m)",
            "Date Installed": "(CCYY-MM-DDThh:mmZ)",
            "Date Removed": "(CCYY-MM-DDThh:mmZ)",
            "Additional Information": "(multiple lines)",
        }
        return data

    @property
    def antenna_type(self):
        return self._data["Antenna Type"]

    @antenna_type.setter
    def antenna_type(self, value):
        if len(value) > 20:
            raise ValueError(
                "Antenna Type from rcvr_ant.tab must be no longer than 20 characters long"
            )
        self._data["Antenna Type"] = value

    @property
    def serial_number(self):
        return self._data["Serial Number"]

    @serial_number.setter
    def serial_number(self, value):
        self._data["Serial Number"] = value

    @property
    def antenna_reference(self):
        return self._data["Antenna Reference Point"]

    @antenna_reference.setter
    def antenna_reference(self, value):
        self._data["Antenna Reference Point"] = value

    @property
    def up(self):
        return self._data["Marker->ARP Up Ecc. (m)"]

    @up.setter
    def up(self, value):
        if type(value) is str:
            if re.match(r"^[\d\.]+$", value):
                value = "{:8.4f}".format(float(value))
            elif re.match(r"^[\d\.]+\s*[^0-9.]+$", value):
                value = "{:8.4f}".format(float(re.sub(r"\s*[^0-9.]+", "", value)))
        elif type(value) is float:
            value = "{:8.4f}".format(value)
        self._data["Marker->ARP Up Ecc. (m)"] = value

    @property
    def north(self):
        return self._data["Marker->ARP North Ecc(m)"]

    @north.setter
    def north(self, value):
        if type(value) is str:
            if re.match(r"^[\d\.]+$", value):
                value = "{:8.4f}".format(float(value))
            elif re.match(r"^[\d\.]+\s*[^0-9.]+$", value):
                value = "{:8.4f}".format(float(re.sub(r"\s*[^0-9.]+", "", value)))
        elif type(value) is float:
            value = "{:8.4f}".format(value)
        self._data["Marker->ARP North Ecc(m)"] = value

    @property
    def east(self):
        return self._data["Marker->ARP East Ecc(m)"]

    @east.setter
    def east(self, value):
        if type(value) is str:
            if re.match(r"^[\d\.]+$", value):
                value = "{:8.4f}".format(float(value))
            elif re.match(r"^[\d\.]+\s*[^0-9.]+$", value):
                value = "{:8.4f}".format(float(re.sub(r"\s*[^0-9.]+", "", value)))
        elif type(value) is float:
            value = "{:8.4f}".format(value)
        self._data["Marker->ARP East Ecc(m)"] = value

    @property
    def north_alignment(self):
        return self._data["Alignment from True N"]

    @north_alignment.setter
    def north_alignment(self, value):
        self._data["Alignment from True N"] = value

    @property
    def radome_type(self):
        return self._data["Antenna Radome Type"]

    @radome_type.setter
    def radome_type(self, value):
        if len(value) > 4:
            raise ValueError("Antenna Radome Type must be 4 characters long")
        self._data["Antenna Radome Type"] = value

    @property
    def radome_serial(self):
        return self._data["Radome Serial Number"]

    @radome_serial.setter
    def radome_serial(self, value):
        self._data["Radome Serial Number"] = value

    @property
    def cable_type(self):
        return self._data["Antenna Cable Type"]

    @cable_type.setter
    def cable_type(self, value):
        self._data["Antenna Cable Type"] = value

    @property
    def cable_length(self):
        return self._data["Antenna Cable Length"]

    @cable_length.setter
    def cable_length(self, value):
        self._data["Antenna Cable Length"] = value

    @property
    def date_installed(self):
        return self._data["Date Installed"]

    @date_installed.setter
    def date_installed(self, value):
        if isinstance(value, dt):
            try:
                value = value.strftime("%Y-%m-%dT%H:%M%Z")
            except:
                value = value.strftime("%Y-%m-%d")
        elif value == "":
            pass
        else:
            datetime_object = None
            time_formats = ["%Y-%m-%dT%H:%M%Z", "%Y-%m-%dT%H:%MZ", "%Y-%m-%d"]

            for format in time_formats:
                try:
                    datetime_object = dt.strptime(value, format)
                    break
                except:
                    continue

            if datetime_object is None:
                raise ValueError("Incorrect date format, should be (CCYY-MM-DDThh:mmZ)")
        self._data["Date Installed"] = value

    @property
    def date_removed(self):
        return self._data["Date Removed"]

    @date_removed.setter
    def date_removed(self, value):
        if isinstance(value, dt):
            try:
                value = value.strftime("%Y-%m-%dT%H:%M%Z")
            except:
                value = value.strftime("%Y-%m-%d")
        elif value == "":
            pass
        else:
            datetime_object = None
            time_formats = ["%Y-%m-%dT%H:%M%Z", "%Y-%m-%dT%H:%MZ", "%Y-%m-%d"]

            for format in time_formats:
                try:
                    datetime_object = dt.strptime(value, format)
                    break
                except:
                    continue

            if datetime_object is None:
                raise ValueError("Incorrect date format, should be (CCYY-MM-DDThh:mmZ)")
        self._data["Date Removed"] = value

    @property
    def additional(self):
        return self._data["Additional Information"]

    @additional.setter
    def additional(self, value):
        self._data["Additional Information"] = value

    def string(self):
        self.additional = _format_string(self.additional, "multilinevalue")
        self.subsectionheader = _format_string(
            "Antenna Type", "subsectitle", len(str(self.subtitle))
        )
        section_text = f"""
4.{self.subtitle}{self.subsectionheader}{self.antenna_type}
     Serial Number            : {self.serial_number}
     Antenna Reference Point  : {self.antenna_reference}
     Marker->ARP Up Ecc. (m)  : {self.up}
     Marker->ARP North Ecc(m) : {self.north}
     Marker->ARP East Ecc(m)  : {self.east}
     Alignment from True N    : {self.north_alignment}
     Antenna Radome Type      : {self.radome_type}
     Radome Serial Number     : {self.radome_serial}
     Antenna Cable Type       : {self.cable_type}
     Antenna Cable Length     : {self.cable_length}
     Date Installed           : {self.date_installed}
     Date Removed             : {self.date_removed}
     Additional Information   : {self.additional}
"""
        return section_text


class Antenna(SectionList):
    def __init__(self):
        super().__init__()
        self._data = self._template_dict()
        self.subsection_type = AntennaType
        self.section_type = "subsectionheader"

    def _template_dict(self):
        data = {
            "Antenna Type": "(A20, from rcvr_ant.tab; see instructions)",
            "Serial Number": "(A*, but note the first A5 is used in SINEX)",
            "Antenna Reference Point": '(BPA/BCR/XXX from "antenna.gra"; see instr.)',
            "Marker->ARP Up Ecc. (m)": "(F8.4)",
            "Marker->ARP North Ecc(m)": "(F8.4)",
            "Marker->ARP East Ecc(m)": "(F8.4)",
            "Alignment from True N": "(deg; + is clockwise/east)",
            "Antenna Radome Type": "(A4 from rcvr_ant.tab; see instructions)",
            "Radome Serial Number": "",
            "Antenna Cable Type": "(vendor & type number)",
            "Antenna Cable Length": "(m)",
            "Date Installed": "(CCYY-MM-DDThh:mmZ)",
            "Date Removed": "(CCYY-MM-DDThh:mmZ)",
            "Additional Information": "(multiple lines)",
        }
        return data

    def string(self):

        section_text = f"""
4.   GNSS Antenna Information
"""
        if self._subsections:
            for subsection in self._subsections:
                section_text += subsection.string()
        else:
            s = AntennaType()
            s.subtitle = "x"
            section_text += s.string()

        return section_text
