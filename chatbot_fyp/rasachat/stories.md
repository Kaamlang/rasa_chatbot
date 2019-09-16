## start path
* start_begin
  - utter_start_begin

## greeting path
* greet
  - utter_greet

## greeting path1
* greet
  - utter_greet
* greet_reply
  - utter_greet_qsn

## say goodbye
* goodbye
  - utter_goodbye

## thanking
* thanking
  - utter_thanking

## sorry
* sorry
  - utter_sorry

## deny path
* greet
  - utter_greet
* deny
  - utter_deny
* deny
  - utter_deny2

## deny2 path
* deny
  - utter_deny
* deny
  - utter_deny2

## superdeny path2
* superdeny
  - utter_superdeny

## suprdeny path
* superdeny
  - utter_deny

## suprdeny path2
* superdeny
  - utter_deny2

## ok
* ok
  - utter_ok

## botinfo
* name
  - utter_name

## collegename
* collegename
  - utter_collegename

## address path
* address
  - utter_address
  - utter_moreinfo

## uniname path
* university_name{"uniname":"university"}
  - utter_university_name

## unidetail path
* universitydetail{"uniname":"university", "info":"information"}
  - utter_universitydetail

## course_query path 1
* course{"bachelor":"bachelor", "course":"program", "offered": "offered"}
  - utter_course

## admission_cost path
* admission_cost{"admit":"admission", "cost":"fee"}
  - utter_admission_cost

## admission path
* admission_req{"admit":"admission", "criteria":"requirement"}
  - utter_admission_req
  - utter_moreinfo

## admission deadline
* deadline
  - utter_deadline
  - utter_moreinfo

## query path
* query{"bachelor": "bachelor"}
  - utter_query

## query path2
* query{"bachelor": "bachelor", "program":"program"}
  - utter_query

## course1
* 1course{"subject":"subject", "year":"first"}
  - utter_1course

## course2
* 2course{"subject":"subject", "year":"second"}
  - utter_2course

## course3
* 3course{"subject":"subject", "year":"third"}
  - utter_3course

## course_fee path
* course_cost{"course":"course", "cost":"fee"}
	- utter_course_cost

## course query
* course_query
  - utter_course_query

## coursecost_1
* 1course_cost
	- utter_1course_cost

## coursecost_2
* 2course_cost
	- utter_2course_cost

## coursecost_3
* 3course_cost
	- utter_3course_cost

## scholarships
* scholarship
  - utter_scholarship

## discount path
* discount
  - utter_discount

## affiliation
* affiliation
  - utter_affiliation

## duration path
* duration{"course":"course", "time":"duration"}
  - utter_duration

## 1stsem path
* 1stsem
  - utter_1stsem

## 2ndsem path
* 2ndsem
  - utter_2ndsem

## 3rdsem path
* 3rdsem
  - utter_3rdsem

## 4thsem path
* 4thsem
  - utter_4thsem

## 5thsem path
* 5thsem
  - utter_5thsem

## 6thsem path
* 6thsem
  - utter_6thsem

## futurescope
* futurescope
  - utter_futurescope

## extra path
* extra{"extra":"extra", "cocu":"co-curricular", "event":"activity"}
  - utter_extra

## games path
* game{"game":"game"}
  - utter_game
  - utter_moreinfo

## eduevent path
* education_event{"event":"event"}
  - utter_education_event

## teaching path
* teaching{"teach":"teaching", "method":"method"}
  - utter_teaching
  - utter_moreinfo

## lab path
* lab{"lab":"lab"}
  - utter_lab

## specific path
* specific
  - utter_specific

## entrance path
* entrance 
  - utter_entrance
  - utter_moreinfo

## timing path
* classtiming
  - utter_classtiming
  - utter_moreinfo

## collegetiming path
* collegetiming
  - utter_collegetiming
  - utter_moreinfo

## semfeee
* semfee
  - utter_semfee