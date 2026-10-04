def shutdown():
        print("Shutting down the system...")
decisionshutdown = input("Are you sure you want to shut down the system? (yes/no): ")
if decisionshutdown.lower() == "yes":
        print("System is shutting down...")
else:
        if decisionshutdown.lower() == "no":
            print("Shutdown canceled.")