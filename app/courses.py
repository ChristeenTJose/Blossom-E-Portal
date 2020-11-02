courses = []

def add_course(count,courseName,price,courseDescription):
	global courses,courses_index
	post = {"_id": count, "courseName": courseName, "price": price, "courseDescription": courseDescription}
	courses.append(post)

price = "50,000(100 hrs)"#	Soft skills

count = 1
courseName = "Employment Skills"
courseDescription = "Employability skills are the core skills and traits needed in nearly every job."
courseDescription += " These are the general skills that make someone desirable to an organization."
courseDescription += " Hiring managers almost always look for employees with these skills."
courseDescription += " Employability skills are sometimes called foundational skills or job-readiness skills."
courseDescription += " Employability skills include the soft skills that allow you to work well with others, apply knowledge to solve problems, and to fit into any work environment."
courseDescription += " They also include the professional skills that enable you to be successful in the workplace."
courseDescription += "These are also considered as transferable skills because you can apply them to a job in any industry."
add_course(count,courseName,price,courseDescription)

count+=1
courseName = "Communication Skills"
courseDescription = "Being able to communicate effectively is perhaps the most important of all life skills."
courseDescription += " It is what enables us to pass information to other people, and to understand what is said to us."
courseDescription += " You only have to watch a baby listening intently to its mother and trying to repeat the sounds that she makes to understand how fundamental is the urge to communicate."
courseDescription += " Communication skills may take a lifetime to master—if indeed anyone can ever claim to have mastered them."
courseDescription += " There are, however, many things that you can do fairly easily to improve your communication skills and ensure that you are able to transmit and receive information effectively."
courseDescription += " Developing your communication skills can help all aspects of your life, from your professional life to social gatherings and everything in between."
add_course(count,courseName,price,courseDescription)

count+=1
courseName = "Personal Skills"
courseDescription = "Candidates with strong personal skills are in high demand for a wide variety of jobs."
courseDescription += " We’ve all worked with someone who is excellent at engaging with colleagues and is always dependable."
courseDescription += " This individual has honed their personal skills." 
courseDescription += " They communicate effectively with others, self-express, and self-manage."
courseDescription += " Unlike hard skills that can be measured, like computer programming skills or legal knowledge, personal skills are soft skills—intangible qualities or traits that enhance our interactions."
courseDescription += " They are just as, if not more, important to employers, though you'll need a mix of both."
add_course(count,courseName,price,courseDescription)

count+=1
courseName = "Professional Skills"
courseDescription = "If you want to be successful in any field, being a professional is essential." 
courseDescription += " But being a professional requires more than having specialized knowledge or dressing appropriately for the situation."
courseDescription += " Professional skills are career competencies that often are not taught (or acquired) as part of the coursework required to earn your masters or PhD."  
courseDescription += " Professional skills such as leadership, mentoring, project management, and conflict resolution are value-added skills essential to any career." 
courseDescription += " While earning your degree, you'll need to hone competencies such as Collaboration and Teamwork, Leadership, Mentoring, Negotiation and Conflict Management, Project Management, Productive Meeting Management."
add_course(count,courseName,price,courseDescription)

count+=1
courseName = "Social Skills"
courseDescription = " The purpose of this course is to enhance social competence ."
courseDescription += " It is done through explicit instruction of skills necessary to engage in successful communication, enhance self-awareness, and navigate the social world both in and out of the classroom atmosphere. "
courseDescription += " Students' IEP goals will also be incorporated into the lessons."
add_course(count,courseName,price,courseDescription)

count+=1
courseName = "Attitudinal Skills"
courseDescription = "T he intent of attitudinal training is to influence or persuade a person to make a decision in the desired direction."
courseDescription += " Changing attitudes can take time and may require multiple points of contact, reminders and the occasional motivational push. "
courseDescription += " But it also lends itself to many creative approaches."
courseDescription += " It may involve changing attitudes as well as associated feelings, values, motivations and beliefs."
add_course(count,courseName,price,courseDescription)

count+=1
courseName = "Organizational Skills"
courseDescription = " During this training course, participants develop an understanding and use of examining their habits and routines, prioritizing, organizing the workspace and setting plans to stay organized. "
courseDescription += " It also helps to identify and remove obstacles to organization and productivity such as procrastination."
courseDescription += " Having a super organized team leader, manager, or head of business can greatly influence your own actions and behavior."
courseDescription += " Possessing organizational skills enables you to get back control of your tasks when you’re feeling overwhelmed and perform better at work. "
add_course(count,courseName,price,courseDescription)

count+=1
courseName = "21st Century skills"
courseDescription = "This refers to abroad set of knowledge, skills,and character traits that are believed—by educators, school reformers, collegeand others—to be critically important to success in today’s world"
courseDescription += " On the basis of the historical development of 21st Century Skills, it consist of three skill sets or 3 Ls - namely, Learning Skills, Life Skills and Literacy Skills"
courseDescription += " These are important for Children with Special Needs for developing their independence in their home, school, and community environments."
courseDescription += " The driving force for the 21st century is the intellectual capital of citizens"
add_course(count,courseName,price,courseDescription)

count+=1
courseName = "Literacy Skills"
courseDescription = "In this course, educators will examine the role of literature in literacy learning.  "
courseDescription += " Emphases will be on the promotion of wide reading in a variety of genres and attending to the appropriate selection of literature to meet reading interests, needs, and abilities of elementary students."
courseDescription += " This dedicated session of literacy instruction helps students learn to match their information needs to appropriate source types and the search tools to find those sources. "
add_course(count,courseName,price,courseDescription)

count+=1
courseName = "Public Speaking Skills"
courseDescription = "This course is an introduction to speech communication which emphasizes the practical skill of public speaking, including techniques to lessen speaker anxiety, and the use of visual aids to enhance speaker presentations."
courseDescription += " The courses in this specializations should help speakers at all levels."
courseDescription += " This specialization will provide you with the instruction, experience, and practice to develop and deliver compelling presentations."
courseDescription += " By the end of the course, you should be able to significantly reduce your fear of public speaking, use rehearsal techniques to develop a strong,  and perform speeches with dynamic movement and gestures. "
add_course(count,courseName,price,courseDescription)

count+=1
courseName = "Methodical Skills"
courseDescription = "With this course one can evaluate and interpret evidence of different types, including documentary and other qualitative sources as well as statistical data."
courseDescription += " He/She can also explain the respective roles of, and interaction between, questions, theories, evidence and explanations in the social sciences."
courseDescription += " It will help to Analyse contemporary social problems using theoretical perspectives from more than onesocial science discipline. "
add_course(count,courseName,price,courseDescription)

count+=1
courseName = "The art of Delegation"
courseDescription = " Delegating prepares employees who work for you to be able to handle your responsibilities and simultaneously allows you to advance to other career opportunities within your organization."
courseDescription += "After you complete this Delegating Effectively training course, you will be able to:"
courseDescription += " a. Clearly identify how delegation fits into your job and how it can make you more successful"
courseDescription += " b. Recognize common delegation pitfalls and how to avoid them "
courseDescription += " c. Give better instructions for better delegation results"
add_course(count,courseName,price,courseDescription)

count+=1
courseName = "Assertive skills"
courseDescription = "The course offers participants the opportunity to work on their own personal and work situations, where they want to be more assertive. "
courseDescription += " As a result, participants leave our assertiveness skills training equipped with some effective, practised strategies for achieving a more successful outcome."
courseDescription +="  This course is ideal for people looking to take more control of their working and/or personal life. "
courseDescription += " By the end of this one-day course, the participants will have created an action plan to enable them to build on their new assertiveness skills going forward."

add_course(count,courseName,price,courseDescription)

count+=1
courseName = "Presentation skills"
courseDescription = "This course helps participants discover how to craft presentations around essential objectives, present key concepts and ideas with power and enthusiasm."
courseDescription += " It will help to design and present effective visuals, and employ techniques for polishing and mastering presentation delivery."
courseDescription += " Our courses are designed for anyone from a rookie speaker to an established presenter. Whether you’re presenting any topic , this gives you tools to make it right."
add_course(count,courseName,price,courseDescription)


price = "10000 (per day)"#	Training Programmes

count+=1
courseName = "English Grammar Training"
courseDescription = "Take English grammar lessons to understand parts of speech, interjections, past tense rules, simple present, verb tenses, action verbs, complex sentences, and more."
courseDescription += " These courses are designed to help you increase your knowledge of grammar and make you less reliant on using apps and plug-ins to check grammar when sending emails at work."
courseDescription += " Start learning its proper usage and demonstrate your English skills to enhance your personal, career, and social development."
add_course(count,courseName,price,courseDescription)

count+=1
courseName = "Training Programmes for Schools and Colleges"
courseDescription = "With technology covering most of the industries today under its huge umbrella, it has become mandatory for students and professionals to be skilled in the trending technology."
courseDescription += " We not only train the students in schools but also deliver capacity building training to schools. In addition, we provide effective Management and Leadership training to Principals, Vice Principals and Heads of institutions. "
courseDescription += " This course also provides comprehensive end-to- end solutions in the skills assessment domain."
courseDescription += " The programmes focused on training across a wide range of functions including preparation of assessment frameworks, developing materials, teacher training and development of professional standards. "
add_course(count,courseName,price,courseDescription)



price = "600 (per hour)"#	Professional Language Consulting

count+=1
courseName = "Spoken English"
courseDescription = "This course will help you reach that goal. Speak English Professionally: In person, Online and On the Phone will boost your English speaking skills."
courseDescription += " Throughout the course, you will adjust how you speak English and you will become more fluent and accurate when you speak. "
courseDescription += " You will demonstrate  culturally appropriate body language and tone. As you work through the course, you will complete self- and peer-evaluations. "
courseDescription += " Through a combination of lectures, comprehension and vocabulary quizzes, practice and performance, you’ll gain the skills and confidence to communicate well  in English."
courseDescription += "  By the end of this course you will change how you speak English"
add_course(count,courseName,price,courseDescription)

count+=1
courseName = "Essential Grammar for placements"
courseDescription = "English grammar is essential to promoting communication, both verbally and in writing."
courseDescription += " Start learning its proper usage and demonstrate your English skills to enhance your personal, career, and social development."
courseDescription += " Improve your knowledge of the English language and pronunciation and practice your speaking and vocabulary with our video lessons."
add_course(count,courseName,price,courseDescription)

count+=1
courseName = "Verbal reasoning"
courseDescription = "This course was designed for people who are about to face the Verbal Reasoning test. It is comprised of sample tests and tailored questionnaires that will boost your Verbal level over time."
courseDescription += " The course includes practical reading strategies to allow you to quickly and effectively comprehend  test question data."
courseDescription += " For most competitive exams, the verbal ability section is one where a candidate can score more yet tends to lose marks due to the varied options provided."
add_course(count,courseName,price,courseDescription)

count+=1
courseName = "Writing Strategies"
courseDescription = "This course describes the purpose of writing assignments and what an instructor might expect to see from your writing "
courseDescription += " It identify common types of writing tasks in a college class."
courseDescription += " It understand and utilize writing-process steps for the development of academic writing."
courseDescription += " It differentiate between revision and proofreading, and explain the value of each"
add_course(count,courseName,price,courseDescription)

count+=1
courseName = "LSRW Skills"
courseDescription = "The objective to enhance the learner’s communication skills by giving adequate exposure in LSRWlistening, speaking, reading and writing skills and the related sub-skills."
courseDescription = " It enables the learner to achieve adequate linguistic skills to help him compete international certification tests of English such as IELTS and TOEFL."
courseDescription = ""
add_course(count,courseName,price,courseDescription)

count+=1
courseName = "Interview Skills"
courseDescription = "Master your interviewing skills with this comprehensive course from TeachUcomp, Inc. Mastering Your Interview Made Easy features. Watch, listen and learn as your expert instructor guides you through each lesson step-by-step. "
courseDescription += " During this media-rich learning experience, you will see each lesson just as if your instructor were there with you. "
courseDescription += " You will learn what to do before your interview is scheduled, specific interviewing techniques and you will have the opportunity to practice the most common interview questions."
courseDescription += " This course will empower you with the knowledge and skills necessary to dazzle during your next interview."
courseDescription += " We have incorporated years of classroom training experience and teaching techniques to develop an easy-to-use course that you can customize to meet your personal learning needs. "
add_course(count,courseName,price,courseDescription)


price = "600 (per hour)"#	Mentoring and Career Coaching

count+=1
courseName = "Learning Skills"
courseDescription = "Learning skills are the skills you need to enable you to study and learn efficiently – they are an important set of transferable life skills."
courseDescription +=  " We provide generic study skills advice – appropriate to learners across all disciplines and in different life circumstances: full and part-time students, those engaged in professional development and anybody who wants to learn how to learn effectively. "
courseDescription += " This will increase your awareness of how you study and you’ll become more confident.  Once mastered, study skills will be beneficial throughout your life."
add_course(count,courseName,price,courseDescription)

count+=1
courseName = "Life Skills"
courseDescription = "The objective of this course is to familiarize students with basic aspects of life skills and its conceptual treatment, theoretical perspectives and practical strategies of life skills education. "
courseDescription +=  " The course aims to provide systematic understanding of the theoretical basis of life skill education, application of life skill to the present day complicated contemporary living system and Professionalization of life skill education. "
courseDescription +=  " The course can be well utilized for all prospective teachers as an inevitable course at any level."
courseDescription += " After completing the course, the learner is expected to master in developing life skills and applying it in various spheres of life."
add_course(count,courseName,price,courseDescription)

count+=1
courseName = "Personal and Professional Etiquettes"
courseDescription = "From this course ,participants will learn what “professionalism” is, tips on how to increase their professionalism, make a good first impression, and how to demonstrate “social savvy” ."
courseDescription += " It's objective is having a proper posture both in the professional environment as well as in one’s social life"
courseDescription += " It helps in improving the quality of the individual’s personal and professional life"
add_course(count,courseName,price,courseDescription)

count+=1
courseName = "Work Ethics"
courseDescription = "The course orients students toward issues that are important in professional counselling, including: - Ethical issues; - Accountability; - Legal issues, including professional indemnity. "
courseDescription += " It aims to provide scope for the application of knowledge and skills either in the context of the student's own workplace or that of a suitable agency, institution or service in which the counselling of clients can occur. "
courseDescription += " This helps to develop and demonstrate their capacity to communicate ethical concepts and justify informed clinical decisions through reference to appropriate ethical theories, models and/or principles."
courseDescription += " Also provides guidence to recognise and critically reflect on a range of ethical issues, and ethical dilemmas in contemporary counselling practice"
add_course(count,courseName,price,courseDescription)

count+=1
courseName = "GK and Current Affairs Training"
courseDescription = " General Knowledge (GK) is very important area in all the competitive exam held in the country. Most of the aspirants feel difficulty in scoring good marks in it. "
courseDescription += " It aims to provide mass online education programme that will provide free online courses by giving access to high quality, IIT-style education to Indian students in Indian language."
courseDescription += " The students will get an honour certificate of achievement certifying successful completion of the course after they have qualified in the tests."
add_course(count,courseName,price,courseDescription)

count+=1
courseName = "Foundation classes for Civil Service"
courseDescription = "The FOUNDATION COURSE is designed to: Create awareness about the Civil services Examination conducted by UPSC."
courseDescription += " Works to equip the students with the basic preparation strategies for the Civil Services examination (IAS)"
courseDescription += "This course consists of classroom lectures by experienced faculty, high-quality study materials, talks by senior civil service officers, as well as a UPSC test series to assess your skills."
courseDescription += " It provides an overview on all subjects / topics in the syllabus of Preliminary Examination in-depth."
add_course(count,courseName,price,courseDescription)

count+=1
courseName = "Motivational Classes"
courseDescription = "This  online self motivation course will give you teach you about the most effective ways to motivate yourself and others. "
courseDescription += " Motivation is the master skill of success - without it, you will fail, but with it, you can find success! In this course you will learn how to build a motivational mindset and acquire the skills to destroy any demotivators that have been holding you back."
courseDescription += " This  course is based on scientific research & principles that are known to get results fast! Having these tools & strategies will make becoming successful so much easier, dramatically increase the results you get & help you achieve your goals in far less time. "
add_course(count,courseName,price,courseDescription)


price = "450 (per hour)"

count+=1
courseName = "English Tutoring"
courseDescription = "Tutors are a fantastic resource for learning English. They’re not just for people who are having problems learning English—anyone can benefit from having a tutor."
courseDescription += " Classes take place over Skype, and a clear rating system with reviews makes it easy to see what people liked and disliked about any tutor."
courseDescription += " So, by taking English classes ,one can  become a part of our big language learning community where one will be able to ask anyone for tips and queries."
add_course(count,courseName,price,courseDescription)


if __name__ == "__main__":
	for i in courses:
		print(i,'\n\n')
