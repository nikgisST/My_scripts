import os

STORED_FILENAME = "stored_filename"
ORIGINAL_FILENAME = "original_filename"


class ExposureSummary(dict):
    def __init__(self, location, size, created_date):
        super(ExposureSummary, self).__init__(
            {'location': location, 'size': size, 'created_date': created_date}
        )

    @property
    def location(self):
        return self['location']

    @property
    def size(self):
        return self['size']

    @property
    def created_date(self):
        return self['created_date']


class OutputsSummary(object):

    def __init__(self, location, size, created_date):
        self.location = location
        self.size = size
        self.created_date = created_date


class AnalysisStatus(dict):
    def __init__(self, _id, status, message, outputs_location):
        super(AnalysisStatus, self).__init__(
            {'id': _id, 'status': status, 'message': message, 'outputs_location': outputs_location,}
        )

    @property
    def id(self):
        return self['id']

    @property
    def status(self):
        return self['status']

    @status.setter
    def status(self, value):
        self['status'] = value

    @property
    def message(self):
        return self['message']

    @property
    def outputs_location(self):
        return self['outputs_location']


path = r'C:\Users\New\Downloads'
file_name = 'nhess-21-393-2021.pdf'
full_path = os.path.join(path, file_name)
exposure = ExposureSummary(location=full_path, size=4758, created_date='2024-07-30')

# Access properties
print(exposure.location)  # C:\Users\New\Downloads\nhess-21-393-2021.pdf
print(exposure.size)  # 4758
print(exposure.created_date)  # 2024-07-30
print()

#file_name = os.path.basename(full_path)
#directory = os.path.dirname(full_path)
#print(directory)   -->       C:\Users\New\Downloads
#print(file_name)   -->       nhess-21-393-2021.pdf
#print(exposure['location'])  with a dictionary methods

######################################################################################

# Create an instance of OutputsSummary
outputs = OutputsSummary(location='D:\ESRI', size=4096, created_date='2017-08-09')

# Access attributes directly
print(outputs.location)        # D:\ESRI
print(outputs.size)            # 4096
print(outputs.created_date)    # 2017-08-09

# Directly modifying attributes
outputs.location = 'D:\ESRI\\new_output'
print(outputs.location)        # Output: /new/path/to/output
print()

##################################################################################################

# Create an instance of AnalysisStatus
analysis_status = AnalysisStatus(
    _id='1000',
    status='Processing',
    message='The analysis is underway.',
    outputs_location='D:\ESRI\\new_output\\analysis\output'
)

# Access properties
print(analysis_status.id)                # 1000
print(analysis_status.status)            # Processing
print(analysis_status.message)           # The analysis is underway.
print(analysis_status.outputs_location)  # D:\ESRI\new_output\analysis\output

# Modify status using the setter
analysis_status.status = 'Completed'
print(analysis_status.status)            # Completed

# You can also use dictionary methods if needed
print(analysis_status['message'])         # The analysis is underway.


# PURPOSES:
# Scenario: File Inventory System
# to track files in a directory, their sizes and creation dates
# to be scheduled to run periodically and update a log or database with this information
# to help collect metadata about files

#Scenario: Analyzing File Size Trends
# to analyze trends related to file sizes or file system usage over time
# to monitor the growth of log files to forecast storage needs
# to regularly collect file sizes and then analyze the trends in the collected data
# to gather data and then perform statistical analysis

#Scenario: Backup Verification
# to verify the size and existence of backup files in an automated backup system to ensure they are created successfully and are not corrupted
# to check backup files exist ann to compare their sizes against expected values for an integrity of backups

#Scenario: Migrating Files Between Systems
# to migrating files from one system to another and to gather metadata about the files ensuring they are copied correctly.
