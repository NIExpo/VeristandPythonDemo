import niveristand
import subprocess
from niveristand.legacy import NIVeriStand
from niveristand.errors import RunError
from niveristand import nivs_rt_sequence, NivsParam, realtimesequencetools, clientapi, run_py_as_rtseq
from niveristand.clientapi import BooleanValue, ChannelReference, DoubleValue
from niveristand.library import wait
from examples.engine_demo.engine_demo_basic import run_engine_demo
from examples.engine_demo.engine_demo_advanced import run_engine_demo_advanced
import os
from time import sleep

#Create Variable to use within the code to set RPM
setRPM = 2500
file_path = r"C:\Users\ahidalgo\Documents\VeriStand Projects\Engine Demo\Engine Demo.nivsproj"

#Start NI VeriStand
os.startfile(file_path)
sleep(17)

#Open the Workspace, this is to use the Legacy functionality to manipulate the controls and indicators in the project
workspace = NIVeriStand.Workspace2('localhost')

#engine_demo_path = r'C:\Users\Public\Documents\National Instruments\NI VeriStand 2020\Examples\Stimulus Profile\Engine Demo\Engine Demo.nivssdf'
engine_demo_path = r'C:\Users\ahidalgo\Documents\VeriStand Projects\Engine Demo\Engine Demo.nivssdf'

try:
    #Initiate Connection and Deploy a Sysem Definition File
    workspace.ConnectToSystem(engine_demo_path, True, 60000)
    sleep(4)

    run_py_as_rtseq(run_engine_demo)
    print("Test Success")

    run_py_as_rtseq(run_engine_demo_advanced)
    print("Advanced Test Success")
    # #Turn on the Engine
    # workspace.SetSingleChannelValue("EnginePower", 1)
    # #Iterate 10 time, changing the desired RPM and reading the actual value
    # for i in range(10):
    #     workspace.SetSingleChannelValue("DesiredRPM", setRPM)
    #     #Give time for the model to process the change and report back
    #     sleep(1)
    #     #Read the Actual RPM Indicator
    #     ActualRPM = workspace.GetSingleChannelValue("ActualRPM")
    #     print("ActualRPM: ", ActualRPM)
    #     #Increase the Desired RPM
    #     setRPM = setRPM+100
    # #Slow down the engine and power off
    # workspace.SetSingleChannelValue("DesiredRPM", 0)
    # workspace.SetSingleChannelValue("EnginePower", 0)
    # You can now disconnect from the system, so the next test can run.


except RunError as e:
    print("Test Failed: %d -  %s" % (str(e.error.error_code), e.error.message))
finally:
    # You can now disconnect from the system, so the next test can run.
    print("End of Test")
    print("Disconnect")
    workspace.DisconnectFromSystem('', True)
