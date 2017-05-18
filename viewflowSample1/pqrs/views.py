from django.shortcuts import render,redirect
from viewflow.flow.views.utils import get_next_task_url

from django.views import generic
from viewflow.flow.views import StartFlowMixin
from formtools.wizard.views import SessionWizardView

from . import forms


class RegisterCustomerClaim(StartFlowMixin, SessionWizardView):
    template_name = "pqrs/manageclaim/start.html"
    form_list = [forms.CustomerForm,forms.ClaimForm]

    def done(self,form_list,form_dict,**kwargs):
        customer = form_dict['0'].save()
        claim = form_dict['1'].save(commit=False)
        claim.customer = customer
        claim.taken_by = self.request.user

        claim.save()

        self.activation.process.claim=claim
        self.activation.done()

        return redirect(get_next_task_url(self.request,self.activation.process))

class testView(generic.TemplateView):
    template_name = "pqrs/index.html"