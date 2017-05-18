from viewflow import flow
from viewflow.base import this, Flow
from . import  views,models,forms
from viewflow.flow.views import UpdateProcessView,CreateProcessView


class ManageClaimFlow(Flow):
    process_class = models.ClaimProcess

    user_claim= flow.Start(
        views.RegisterCustomerClaim
    ).Next(this.type_claim)

    type_claim=flow.View(
        UpdateProcessView,
        form_class=forms.TypeClaimForm
    ).Next(this.split_type_claim)

    split_type_claim=(
        flow.Split()
        .Next(
            this.sample_continue,
            cond=lambda act:act.process.pqr_required
        ).Next(
            this.end,
            cond=lambda act:act.process.s_required
        )
    )
    sample_continue=flow.View(
        views.testView
    ).Next(this.end)

    end = flow.End()
