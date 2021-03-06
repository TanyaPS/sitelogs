from sitelog.sections import Section
import re
from datetime import datetime as dt


class Header:
    def __init__(self, code="XXXX"):
        if not re.match(r"^[A-Z0-9]{4}$", code):
            raise ValueError("The Four Character ID *must* be 4 characters long!")
        self.code = code

    def string(self):
        text = f"""
     {self.code} Site Information Form (site log)
     International GNSS Service
     See Instructions at:
       ftp://igs.org/pub/station/general/sitelog_instr.txt
"""
        return text


class Form(Section):
    def __init__(
        self,
        prepared_by="",
        date="2019-12-12",
        report_type="NEW",
        previous_log="",
        changed_sections="",
    ):
        super().__init__()
        self._data = self._template_dict()
        self.prepared_by = prepared_by
        self.date = date
        self.report_type = report_type
        self.previous_log = previous_log
        self.changed_sections = changed_sections

    def _template_dict(self):
        data = {
            "Prepared by (full name)": "",
            "Date Prepared": "(CCYY-MM-DD)",
            "Report Type": "(NEW/UPDATE)",
            "Update:": "",
            "Previous Site Log": "(ssss_ccyymmdd.log)",
            "Modified/Added Sections": "(n.n,n.n,...)",
        }
        return data

    @property
    def prepared_by(self):
        return self._data["Prepared by (full name)"]

    @prepared_by.setter
    def prepared_by(self, value):
        self._data["Prepared by (full name)"] = value

    @property
    def site_name(self):
        return self._data["Site Name"]

    @site_name.setter
    def site_name(self, value):
        self._data["Site Name"] = value

    @property
    def date(self):
        return self._data["Date Prepared"]

    @date.setter
    def date(self, value):
        if isinstance(value, dt):
            value = value.strftime("%Y-%m-%d")
        elif value == "":
            pass
        else:
            try:
                datetime_object = dt.strptime(value, "%Y-%m-%d")
            except:
                raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        self._data["Date Prepared"] = value

    @property
    def report_type(self):
        return self._data["Report Type"]

    @report_type.setter
    def report_type(self, value):
        if value.upper() not in ("NEW", "UPDATE"):
            raise ValueError("Report type can only be set to 'NEW' or 'UPDATE'")
        self._data["Report Type"] = value

    @property
    def previous_log(self):
        return self._data["Previous Site Log"]

    @previous_log.setter
    def previous_log(self, value):
        self._data["Previous Site Log"] = value

    @property
    def changed_sections(self):
        return self._data["Modified/Added Sections"]

    @changed_sections.setter
    def changed_sections(self, value):
        self._data["Modified/Added Sections"] = value

    def string(self):
        text = f"""
0.   Form

     Prepared by (full name)  : {self.prepared_by}
     Date Prepared            : {self.date}
     Report Type              : {self.report_type}
"""
        update = ""
        if self.report_type == "UPDATE":
            update = f"""
     Update:
      Previous Site Log       : {self.previous_log}
      Modified/Added Sections : {self.changed_sections}"""

        return text.rstrip() + update
