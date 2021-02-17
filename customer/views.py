from django.shortcuts import render
from random import randint

# Create your views here.
import json

def customer(request):
    customer_data={

	"members": [{
			"id": "W012A3CDE",
			"real_name": "Egon Spengler",
			"tz": "America/Los_Angeles",
			"activity_periods": [{
					"start_time": "Feb 1 2020  1:33PM",
					"end_time": "Feb 1 2020 1:54PM"
				},
				{
					"start_time": "Mar 1 2020  11:11AM",
					"end_time": "Mar 1 2020 2:00PM"
				},
				{
					"start_time": "Mar 16 2020  5:33PM",
					"end_time": "Mar 16 2020 8:02PM"
				}
			]
		},
		{
			"id": "W07QCRPA4",
			"real_name": "Glinda Southgood",
			"tz": "Asia/Kolkata",
			"activity_periods": [{
					"start_time": "Feb 1 2020  1:33PM",
					"end_time": "Feb 1 2020 1:54PM"
				},
				{
					"start_time": "Mar 1 2020  11:11AM",
					"end_time": "Mar 1 2020 2:00PM"
				},
				{
					"start_time": "Mar 16 2020  5:33PM",
					"end_time": "Mar 16 2020 8:02PM"
				}
			]
		},
        	{
    			"id": "W067QCRPA4",
    			"real_name": "sundara malik",
    			"tz": "Asia/Kolkata",
    			"activity_periods": [{
    					"start_time": "Mar 1 2020  1:33PM",
    					"end_time": "Mar 1 2020 1:54PM"
    				},
    				{
    					"start_time": "Apr 1 2020  11:11AM",
    					"end_time": "Apr 1 2020 2:00PM"
    				},
    				{
    					"start_time": "May 16 2020  5:33PM",
    					"end_time": "May 16 2020 8:02PM"
    				}
    			]
    		}
	]
}




#dictionary dumped as json in a json file
    with open('Test.json','w') as fp:
     json.dump(customer_data,fp)

    with open('Test.json','r') as fp:
     context2=json.load(fp)
     return render(request,'base.html',{'context':context2})
