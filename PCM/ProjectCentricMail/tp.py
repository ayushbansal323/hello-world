from ProjectCentricMail.models import MessageInfo,ProjectClassify
import csv
import os
#m_id="1664eedf6a81dfe6"
#b="Sunny Khandare <sunnyakhandare5618@gmail.com>"
#c="formal_informal machine learning"
#d="2018-10-06"
#e="Aaditya Deshpande New device signed in to aadityadeshpandeasmi@gmail.com Your Google Account was just signed in to from a new Linux device. You&#39;re getting this email to make sure it was you. Check"
#f=""
#g="ayushbansal323"
#z = MessageInfo(m_id=a,Sender=b,Subject=c,Date=d,Snippet=e,Message_body=f,Username=g)
#c = MessageInfo.objects.filter(m_id=m_id)
#module_dir = os.path.dirname(__file__)
username="ayushbansal323"
f = open(f'{username}_final.csv')
reader = csv.reader(f)
for m_id,Sender,Subject,Date,Snippet,Message_body,is_spam in reader:
	if m_id!="m_id":
		query = MessageInfo.objects.filter(m_id=m_id)
		if not query:
			print(Date)
			tuplem = MessageInfo(m_id=m_id,Sender=Sender,Subject=Subject,Date=Date,Snippet=Snippet,Message_body=Message_body,Username=username)
			tuplem.save()
			mid = MessageInfo.objects.get(m_id=m_id)
			tuplep=ProjectClassify(m_id=mid,Spam=is_spam)
			tuplep.save()
#query = MessageInfo.objects.filter(Username="ayushbansal323")
#c = ProjectClassify.objects.filter(Spam=True).values()
for i in query:
	c = ProjectClassify.objects.filter(m_id=i)
	c.Spam



#https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html


def insert_spam(reader):
    for m_id,Sender,Subject,Date,Snippet,Message_body,is_spam in reader:
    	if m_id!="m_id":
    		query = MessageInfo.objects.filter(m_id=m_id)
    		if not query:
    			print(Date)
    			tuplem = MessageInfo(m_id=m_id,Sender=Sender,Subject=Subject,Date=Date,Snippet=Snippet,Message_body=Message_body,Username=username)
    			tuplem.save()
    			mid = MessageInfo.objects.get(m_id=m_id)
    			tuplep=ProjectClassify(m_id=mid,Spam=is_spam)
    			tuplep.save()
