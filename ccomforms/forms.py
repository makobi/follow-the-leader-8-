from django.contrib.admin import widgets
from ccomforms.models import T02, A125, Profile
from django import forms

'''
Model Form for the Professor's Profile
'''

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile


'''
Add temporary form fields for each element in model array fields.
Render the array fields as separate input fields in the html.
Join these separate input fields before the form saves itself.
'''
class T02Form(forms.ModelForm):

    f10_1 = forms.CharField(max_length=100)
    f11_1 = forms.CharField(max_length=100)
    f12_1 = forms.CharField(max_length=100)
    f13_1 = forms.CharField(max_length=100)
    f14_1 = forms.CharField(max_length=100)
    f15_1 = forms.CharField(max_length=100)
    f16_1 = forms.CharField(max_length=100)
    f17_1 = forms.CharField(max_length=100)
    f18_1 = forms.CharField(max_length=100)
    f19_1 = forms.IntegerField()
    f20_1 = forms.FloatField()
    f20_2 = forms.FloatField()
    f20_3 = forms.FloatField()
    f20_4 = forms.FloatField()
    f20_5 = forms.FloatField()
    f21_1 = forms.CharField(max_length=100)
    f21_2 = forms.CharField(max_length=100)
    f21_3 = forms.CharField(max_length=100)
    f21_4 = forms.CharField(max_length=100)
    f21_5 = forms.CharField(max_length=100)
    f21_6 = forms.CharField(max_length=100)
    f21_7 = forms.CharField(max_length=100)
    f21_8 = forms.CharField(max_length=100)
    f21_9 = forms.CharField(max_length=100)
    f21_10 = forms.CharField(max_length=100)
    f23_1 = forms.CharField(max_length=100)
    f27_1 = forms.CharField(max_length=100)
    f27_2 = forms.CharField(max_length=100)
    f27_3 = forms.CharField(max_length=100)

    class Meta:
        model = T02

    # Magic function that displays ArrayFields as separate input boxes
    def fix_instance(self):
        data10 = ",".join([str(x) for x in self.initial['f10']])
        data10 = data10.split(',')
        self.initial['f10'] = data10[0]
        self.initial['f10_1'] = data10[1]

        data11 = ",".join([str(x) for x in self.initial['f11']])
        data11 = data11.split(',')
        self.initial['f11'] = data11[0]
        self.initial['f11_1'] = data11[1]

        data12 = ",".join([str(x) for x in self.initial['f12']])
        data12 = data12.split(',')
        self.initial['f12'] = data12[0]
        self.initial['f12_1'] = data12[1]

        data13 = ",".join([str(x) for x in self.initial['f13']])
        data13 = data13.split(',')
        self.initial['f13'] = data13[0]
        self.initial['f13_1'] = data13[1]

        data14 = ",".join([str(x) for x in self.initial['f14']])
        data14 = data14.split(',')
        self.initial['f14'] = data14[0]
        self.initial['f14_1'] = data14[1]

        data15 = ",".join([str(x) for x in self.initial['f15']])
        data15 = data15.split(',')
        self.initial['f15'] = data15[0]
        self.initial['f15_1'] = data15[1]

        data16 = ",".join([str(x) for x in self.initial['f16']])
        data16 = data16.split(',')
        self.initial['f16'] = data16[0]
        self.initial['f16_1'] = data16[1]

        data17 = ",".join([str(x) for x in self.initial['f17']])
        data17 = data17.split(',')
        self.initial['f17'] = data17[0]
        self.initial['f17_1'] = data17[1]

        data18 = ",".join([str(x) for x in self.initial['f18']])
        data18 = data18.split(',')
        self.initial['f18'] = data18[0]
        self.initial['f18_1'] = data18[1]

        data19 = ",".join([str(x) for x in self.initial['f19']])
        data19 = data19.split(',')
        self.initial['f19'] = data19[0]
        self.initial['f19_1'] = data19[1]

        data20 = ",".join([str(x) for x in self.initial['f20']])
        data20 = data20.split(',')
        self.initial['f20'] = data20[0]
        self.initial['f20_1'] = data20[1]
        self.initial['f20_2'] = data20[2]
        self.initial['f20_3'] = data20[3]
        self.initial['f20_4'] = data20[4]
        self.initial['f20_5'] = data20[5]

        data21 = ",".join([str(x) for x in self.initial['f21']])
        data21 = data21.split(',')
        self.initial['f21'] = data21[0]
        self.initial['f21_1'] = data21[1]
        self.initial['f21_2'] = data21[2]
        self.initial['f21_3'] = data21[3]
        self.initial['f21_4'] = data21[4]
        self.initial['f21_5'] = data21[5]
        self.initial['f21_6'] = data21[6]
        self.initial['f21_7'] = data21[7]
        self.initial['f21_8'] = data21[8]
        self.initial['f21_9'] = data21[9]
        self.initial['f21_10'] = data21[10]

        data23 = ",".join([str(x) for x in self.initial['f23']])
        data23 = data23.split(',')
        self.initial['f23'] = data23[0]
        self.initial['f23_1'] = data23[1]

        data27 = ",".join([str(x) for x in self.initial['f27']])
        data27 = data27.split(',')
        self.initial['f27'] = data27[0]
        self.initial['f27_1'] = data27[1]
        self.initial['f27_2'] = data27[2]
        self.initial['f27_3'] = data27[3]

    # I use clean to group the array data into one input variable
    def clean(self):
        self.cleaned_data['f10'] = [self.cleaned_data['f10'],self.cleaned_data['f10_1']]
        self.cleaned_data['f11'] = [self.cleaned_data['f11'],self.cleaned_data['f11_1']]
        self.cleaned_data['f12'] = [self.cleaned_data['f12'],self.cleaned_data['f12_1']]
        self.cleaned_data['f13'] = [self.cleaned_data['f13'],self.cleaned_data['f13_1']]
        self.cleaned_data['f14'] = [self.cleaned_data['f14'],self.cleaned_data['f14_1']]
        self.cleaned_data['f15'] = [self.cleaned_data['f15'],self.cleaned_data['f15_1']]
        self.cleaned_data['f16'] = [self.cleaned_data['f16'],self.cleaned_data['f16_1']]
        self.cleaned_data['f17'] = [self.cleaned_data['f17'],self.cleaned_data['f17_1']]
        self.cleaned_data['f18'] = [self.cleaned_data['f18'],self.cleaned_data['f18_1']]
        self.cleaned_data['f19'] = [self.cleaned_data['f19'],self.cleaned_data['f19_1']]
        self.cleaned_data['f20'] = [self.cleaned_data['f20'],self.cleaned_data['f20_1'],self.cleaned_data['f20_2'],self.cleaned_data['f20_3'],self.cleaned_data['f20_4'],self.cleaned_data['f20_5']]
        self.cleaned_data['f21'] = [self.cleaned_data['f21'],self.cleaned_data['f21_1'],self.cleaned_data['f21_2'],self.cleaned_data['f21_3'],self.cleaned_data['f21_4'],self.cleaned_data['f21_5'],self.cleaned_data['f21_6'],self.cleaned_data['f21_7'],self.cleaned_data['f21_8'],self.cleaned_data['f21_9'],self.cleaned_data['f21_10']]
        self.cleaned_data['f23'] = [self.cleaned_data['f23'],self.cleaned_data['f23_1']]
        self.cleaned_data['f27'] = [self.cleaned_data['f27'],self.cleaned_data['f27_1'],self.cleaned_data['f27_2'],self.cleaned_data['f27_3']]

        return self.cleaned_data

'''
Add temporary form fields for each element in model array fields.
Render the array fields as separate input fields in the html.
Join these separate input fields before the form saves itself.
'''

class A125Form(forms.ModelForm):

    sponsored_accounts_1 = forms.CharField(max_length=100)
    sponsored_accounts_2 = forms.CharField(max_length=100)
    sponsored_accounts_3 = forms.CharField(max_length=100)
    sponsored_accounts_4 = forms.CharField(max_length=100)
    sponsored_accounts_5 = forms.CharField(max_length=100)
    sponsored_accounts_6 = forms.CharField(max_length=100)
    sponsored_accounts_7 = forms.CharField(max_length=100)
    sponsored_accounts_8 = forms.CharField(max_length=100)
    sponsored_accounts_9 = forms.CharField(max_length=100)
    sponsored_accounts_10 = forms.CharField(max_length=100)
    sponsored_accounts_11 = forms.CharField(max_length=100)
    sponsored_accounts_12 = forms.CharField(max_length=100)
    sponsored_accounts_13 = forms.CharField(max_length=100)
    sponsored_accounts_14 = forms.CharField(max_length=100)
    sponsored_accounts_15 = forms.CharField(max_length=100)
    sponsored_accounts_16 = forms.CharField(max_length=100)
    sponsored_accounts_17 = forms.CharField(max_length=100)
    sponsored_accounts_18 = forms.CharField(max_length=100)
    sponsored_accounts_19 = forms.CharField(max_length=100)

    cost_sharing_1 = forms.CharField(max_length=100)
    cost_sharing_2 = forms.CharField(max_length=100)
    cost_sharing_3 = forms.CharField(max_length=100)
    cost_sharing_4 = forms.CharField(max_length=100)
    cost_sharing_5 = forms.CharField(max_length=100)
    cost_sharing_6 = forms.CharField(max_length=100)
    cost_sharing_7 = forms.CharField(max_length=100)
    cost_sharing_8 = forms.CharField(max_length=100)
    cost_sharing_9 = forms.CharField(max_length=100)
    cost_sharing_10 = forms.CharField(max_length=100)
    cost_sharing_11 = forms.CharField(max_length=100)
    cost_sharing_12 = forms.CharField(max_length=100)
    cost_sharing_13 = forms.CharField(max_length=100)
    cost_sharing_14 = forms.CharField(max_length=100)

    university_funds_1 = forms.CharField(max_length=100)
    university_funds_2 = forms.CharField(max_length=100)
    university_funds_3 = forms.CharField(max_length=100)
    university_funds_4 = forms.CharField(max_length=100)
    university_funds_5 = forms.CharField(max_length=100)
    university_funds_6 = forms.CharField(max_length=100)
    university_funds_7 = forms.CharField(max_length=100)
    university_funds_8 = forms.CharField(max_length=100)
    university_funds_9 = forms.CharField(max_length=100)
    university_funds_10 = forms.CharField(max_length=100)
    university_funds_11 = forms.CharField(max_length=100)
    university_funds_12 = forms.CharField(max_length=100)
    university_funds_13 = forms.CharField(max_length=100)
    university_funds_14 = forms.CharField(max_length=100)
    university_funds_15 = forms.CharField(max_length=100)
    university_funds_16 = forms.CharField(max_length=100)
    university_funds_17 = forms.CharField(max_length=100)
    university_funds_18 = forms.CharField(max_length=100)
    university_funds_19 = forms.CharField(max_length=100)
    university_funds_20 = forms.CharField(max_length=100)
    university_funds_21 = forms.CharField(max_length=100)
    university_funds_22 = forms.CharField(max_length=100)
    university_funds_23 = forms.CharField(max_length=100)
    university_funds_24 = forms.CharField(max_length=100)

    total_compensation_1 = forms.CharField(max_length=100)

    payments_paid_1 = forms.CharField(max_length=100)
    payments_paid_2 = forms.CharField(max_length=100)
    payments_paid_3 = forms.CharField(max_length=100)
    payments_paid_4 = forms.CharField(max_length=100)
    payments_paid_5 = forms.CharField(max_length=100)
    payments_paid_6 = forms.CharField(max_length=100)
    payments_paid_7 = forms.CharField(max_length=100)
    payments_paid_8 = forms.CharField(max_length=100)

    class Meta:
        model = A125

    # Magic function that fixes how ArrayFields are displayed
    def fix_instance(self):
        sponsored = ",".join([str(x) for x in self.initial['sponsored_accounts']])
        sponsored = sponsored.split(',')
        self.initial['sponsored_accounts'] = sponsored[0]
        self.initial['sponsored_accounts_1'] = sponsored[1]
        self.initial['sponsored_accounts_2'] = sponsored[2]
        self.initial['sponsored_accounts_3'] = sponsored[3]
        self.initial['sponsored_accounts_4'] = sponsored[4]
        self.initial['sponsored_accounts_5'] = sponsored[5]
        self.initial['sponsored_accounts_6'] = sponsored[6]
        self.initial['sponsored_accounts_7'] = sponsored[7]
        self.initial['sponsored_accounts_8'] = sponsored[8]
        self.initial['sponsored_accounts_9'] = sponsored[9]
        self.initial['sponsored_accounts_10'] = sponsored[10]
        self.initial['sponsored_accounts_11'] = sponsored[11]
        self.initial['sponsored_accounts_12'] = sponsored[12]
        self.initial['sponsored_accounts_13'] = sponsored[13]
        self.initial['sponsored_accounts_14'] = sponsored[14]
        self.initial['sponsored_accounts_15'] = sponsored[15]
        self.initial['sponsored_accounts_16'] = sponsored[16]
        self.initial['sponsored_accounts_17'] = sponsored[17]
        self.initial['sponsored_accounts_18'] = sponsored[18]
        self.initial['sponsored_accounts_19'] = sponsored[19]

        cost_sharing = ",".join([str(x) for x in self.initial['cost_sharing']])
        cost_sharing = cost_sharing.split(',')
        self.initial['cost_sharing'] = cost_sharing[0]
        self.initial['cost_sharing_1'] = cost_sharing[1]
        self.initial['cost_sharing_2'] = cost_sharing[2]
        self.initial['cost_sharing_3'] = cost_sharing[3]
        self.initial['cost_sharing_4'] = cost_sharing[4]
        self.initial['cost_sharing_5'] = cost_sharing[5]
        self.initial['cost_sharing_6'] = cost_sharing[6]
        self.initial['cost_sharing_7'] = cost_sharing[7]
        self.initial['cost_sharing_8'] = cost_sharing[8]
        self.initial['cost_sharing_9'] = cost_sharing[9]
        self.initial['cost_sharing_10'] = cost_sharing[10]
        self.initial['cost_sharing_11'] = cost_sharing[11]
        self.initial['cost_sharing_12'] = cost_sharing[12]
        self.initial['cost_sharing_13'] = cost_sharing[13]
        self.initial['cost_sharing_14'] = cost_sharing[14]

        university = ",".join([str(x) for x in self.initial['university_funds']])
        university = university.split(',')
        self.initial['university_funds'] = university[0]
        self.initial['university_funds_1'] = university[1]
        self.initial['university_funds_2'] = university[2]
        self.initial['university_funds_3'] = university[3]
        self.initial['university_funds_4'] = university[4]
        self.initial['university_funds_5'] = university[5]
        self.initial['university_funds_6'] = university[6]
        self.initial['university_funds_7'] = university[7]
        self.initial['university_funds_8'] = university[8]
        self.initial['university_funds_9'] = university[9]
        self.initial['university_funds_10'] = university[10]
        self.initial['university_funds_11'] = university[11]
        self.initial['university_funds_12'] = university[12]
        self.initial['university_funds_13'] = university[13]
        self.initial['university_funds_14'] = university[14]
        self.initial['university_funds_15'] = university[15]
        self.initial['university_funds_16'] = university[16]
        self.initial['university_funds_17'] = university[17]
        self.initial['university_funds_18'] = university[18]
        self.initial['university_funds_19'] = university[19]
        self.initial['university_funds_20'] = university[20]
        self.initial['university_funds_21'] = university[21]
        self.initial['university_funds_22'] = university[22]
        self.initial['university_funds_23'] = university[23]
        self.initial['university_funds_24'] = university[24]

        compensation = ",".join([str(x) for x in self.initial['total_compensation']])
        compensation = compensation.split(',')
        self.initial['total_compensation'] = compensation[0]
        self.initial['total_compensation_1'] = compensation[1]

        payments = ",".join([str(x) for x in self.initial['payments_paid']])
        payments = payments.split(',')
        self.initial['payments_paid'] = payments[0]
        self.initial['payments_paid_1'] = payments[1]
        self.initial['payments_paid_2'] = payments[2]
        self.initial['payments_paid_3'] = payments[3]
        self.initial['payments_paid_4'] = payments[4]
        self.initial['payments_paid_5'] = payments[5]
        self.initial['payments_paid_6'] = payments[6]
        self.initial['payments_paid_7'] = payments[7]
        self.initial['payments_paid_8'] = payments[8]

    def clean(self):
        self.cleaned_data['sponsored_accounts'] = [self.cleaned_data['sponsored_accounts']
        ,self.cleaned_data['sponsored_accounts_1']
        ,self.cleaned_data['sponsored_accounts_2']
        ,self.cleaned_data['sponsored_accounts_3']
        ,self.cleaned_data['sponsored_accounts_4']
        ,self.cleaned_data['sponsored_accounts_5']
        ,self.cleaned_data['sponsored_accounts_6']
        ,self.cleaned_data['sponsored_accounts_7']
        ,self.cleaned_data['sponsored_accounts_8']
        ,self.cleaned_data['sponsored_accounts_9']
        ,self.cleaned_data['sponsored_accounts_10']
        ,self.cleaned_data['sponsored_accounts_11']
        ,self.cleaned_data['sponsored_accounts_12']
        ,self.cleaned_data['sponsored_accounts_13']
        ,self.cleaned_data['sponsored_accounts_14']
        ,self.cleaned_data['sponsored_accounts_15']
        ,self.cleaned_data['sponsored_accounts_16']
        ,self.cleaned_data['sponsored_accounts_17']
        ,self.cleaned_data['sponsored_accounts_18']
        ,self.cleaned_data['sponsored_accounts_19']]
        
        self.cleaned_data['cost_sharing'] = [self.cleaned_data['cost_sharing']
        ,self.cleaned_data['cost_sharing_1']
        ,self.cleaned_data['cost_sharing_2']
        ,self.cleaned_data['cost_sharing_3']
        ,self.cleaned_data['cost_sharing_4']
        ,self.cleaned_data['cost_sharing_5']
        ,self.cleaned_data['cost_sharing_6']
        ,self.cleaned_data['cost_sharing_7']
        ,self.cleaned_data['cost_sharing_8']
        ,self.cleaned_data['cost_sharing_9']
        ,self.cleaned_data['cost_sharing_10']
        ,self.cleaned_data['cost_sharing_11']
        ,self.cleaned_data['cost_sharing_12']
        ,self.cleaned_data['cost_sharing_13']
        ,self.cleaned_data['cost_sharing_14']]

        self.cleaned_data['university_funds'] = [self.cleaned_data['university_funds']
        ,self.cleaned_data['university_funds_1']
        ,self.cleaned_data['university_funds_2']
        ,self.cleaned_data['university_funds_3']
        ,self.cleaned_data['university_funds_4']
        ,self.cleaned_data['university_funds_5']
        ,self.cleaned_data['university_funds_6']
        ,self.cleaned_data['university_funds_7']
        ,self.cleaned_data['university_funds_8']
        ,self.cleaned_data['university_funds_9']
        ,self.cleaned_data['university_funds_10']
        ,self.cleaned_data['university_funds_11']
        ,self.cleaned_data['university_funds_12']
        ,self.cleaned_data['university_funds_13']
        ,self.cleaned_data['university_funds_14']
        ,self.cleaned_data['university_funds_15']
        ,self.cleaned_data['university_funds_16']
        ,self.cleaned_data['university_funds_17']
        ,self.cleaned_data['university_funds_18']
        ,self.cleaned_data['university_funds_19']
        ,self.cleaned_data['university_funds_20']
        ,self.cleaned_data['university_funds_21']
        ,self.cleaned_data['university_funds_22']
        ,self.cleaned_data['university_funds_23']
        ,self.cleaned_data['university_funds_24']]

        self.cleaned_data['total_compensation'] = [self.cleaned_data['total_compensation']
        ,self.cleaned_data['total_compensation_1']]

        self.cleaned_data['payments_paid'] = [self.cleaned_data['payments_paid']
        ,self.cleaned_data['payments_paid_1']
        ,self.cleaned_data['payments_paid_2']
        ,self.cleaned_data['payments_paid_3']
        ,self.cleaned_data['payments_paid_4']
        ,self.cleaned_data['payments_paid_5']
        ,self.cleaned_data['payments_paid_6']
        ,self.cleaned_data['payments_paid_7']
        ,self.cleaned_data['payments_paid_8']]

        return self.cleaned_data

