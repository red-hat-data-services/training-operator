// Copyright 2024 The Kubeflow Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Code generated by client-gen. DO NOT EDIT.

package fake

import (
	"context"
	json "encoding/json"
	"fmt"

	v1 "github.com/kubeflow/training-operator/pkg/apis/kubeflow.org/v1"
	kubefloworgv1 "github.com/kubeflow/training-operator/pkg/client/applyconfiguration/kubeflow.org/v1"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	labels "k8s.io/apimachinery/pkg/labels"
	types "k8s.io/apimachinery/pkg/types"
	watch "k8s.io/apimachinery/pkg/watch"
	testing "k8s.io/client-go/testing"
)

// FakeTFJobs implements TFJobInterface
type FakeTFJobs struct {
	Fake *FakeKubeflowV1
	ns   string
}

var tfjobsResource = v1.SchemeGroupVersion.WithResource("tfjobs")

var tfjobsKind = v1.SchemeGroupVersion.WithKind("TFJob")

// Get takes name of the tFJob, and returns the corresponding tFJob object, and an error if there is any.
func (c *FakeTFJobs) Get(ctx context.Context, name string, options metav1.GetOptions) (result *v1.TFJob, err error) {
	emptyResult := &v1.TFJob{}
	obj, err := c.Fake.
		Invokes(testing.NewGetActionWithOptions(tfjobsResource, c.ns, name, options), emptyResult)

	if obj == nil {
		return emptyResult, err
	}
	return obj.(*v1.TFJob), err
}

// List takes label and field selectors, and returns the list of TFJobs that match those selectors.
func (c *FakeTFJobs) List(ctx context.Context, opts metav1.ListOptions) (result *v1.TFJobList, err error) {
	emptyResult := &v1.TFJobList{}
	obj, err := c.Fake.
		Invokes(testing.NewListActionWithOptions(tfjobsResource, tfjobsKind, c.ns, opts), emptyResult)

	if obj == nil {
		return emptyResult, err
	}

	label, _, _ := testing.ExtractFromListOptions(opts)
	if label == nil {
		label = labels.Everything()
	}
	list := &v1.TFJobList{ListMeta: obj.(*v1.TFJobList).ListMeta}
	for _, item := range obj.(*v1.TFJobList).Items {
		if label.Matches(labels.Set(item.Labels)) {
			list.Items = append(list.Items, item)
		}
	}
	return list, err
}

// Watch returns a watch.Interface that watches the requested tFJobs.
func (c *FakeTFJobs) Watch(ctx context.Context, opts metav1.ListOptions) (watch.Interface, error) {
	return c.Fake.
		InvokesWatch(testing.NewWatchActionWithOptions(tfjobsResource, c.ns, opts))

}

// Create takes the representation of a tFJob and creates it.  Returns the server's representation of the tFJob, and an error, if there is any.
func (c *FakeTFJobs) Create(ctx context.Context, tFJob *v1.TFJob, opts metav1.CreateOptions) (result *v1.TFJob, err error) {
	emptyResult := &v1.TFJob{}
	obj, err := c.Fake.
		Invokes(testing.NewCreateActionWithOptions(tfjobsResource, c.ns, tFJob, opts), emptyResult)

	if obj == nil {
		return emptyResult, err
	}
	return obj.(*v1.TFJob), err
}

// Update takes the representation of a tFJob and updates it. Returns the server's representation of the tFJob, and an error, if there is any.
func (c *FakeTFJobs) Update(ctx context.Context, tFJob *v1.TFJob, opts metav1.UpdateOptions) (result *v1.TFJob, err error) {
	emptyResult := &v1.TFJob{}
	obj, err := c.Fake.
		Invokes(testing.NewUpdateActionWithOptions(tfjobsResource, c.ns, tFJob, opts), emptyResult)

	if obj == nil {
		return emptyResult, err
	}
	return obj.(*v1.TFJob), err
}

// UpdateStatus was generated because the type contains a Status member.
// Add a +genclient:noStatus comment above the type to avoid generating UpdateStatus().
func (c *FakeTFJobs) UpdateStatus(ctx context.Context, tFJob *v1.TFJob, opts metav1.UpdateOptions) (result *v1.TFJob, err error) {
	emptyResult := &v1.TFJob{}
	obj, err := c.Fake.
		Invokes(testing.NewUpdateSubresourceActionWithOptions(tfjobsResource, "status", c.ns, tFJob, opts), emptyResult)

	if obj == nil {
		return emptyResult, err
	}
	return obj.(*v1.TFJob), err
}

// Delete takes name of the tFJob and deletes it. Returns an error if one occurs.
func (c *FakeTFJobs) Delete(ctx context.Context, name string, opts metav1.DeleteOptions) error {
	_, err := c.Fake.
		Invokes(testing.NewDeleteActionWithOptions(tfjobsResource, c.ns, name, opts), &v1.TFJob{})

	return err
}

// DeleteCollection deletes a collection of objects.
func (c *FakeTFJobs) DeleteCollection(ctx context.Context, opts metav1.DeleteOptions, listOpts metav1.ListOptions) error {
	action := testing.NewDeleteCollectionActionWithOptions(tfjobsResource, c.ns, opts, listOpts)

	_, err := c.Fake.Invokes(action, &v1.TFJobList{})
	return err
}

// Patch applies the patch and returns the patched tFJob.
func (c *FakeTFJobs) Patch(ctx context.Context, name string, pt types.PatchType, data []byte, opts metav1.PatchOptions, subresources ...string) (result *v1.TFJob, err error) {
	emptyResult := &v1.TFJob{}
	obj, err := c.Fake.
		Invokes(testing.NewPatchSubresourceActionWithOptions(tfjobsResource, c.ns, name, pt, data, opts, subresources...), emptyResult)

	if obj == nil {
		return emptyResult, err
	}
	return obj.(*v1.TFJob), err
}

// Apply takes the given apply declarative configuration, applies it and returns the applied tFJob.
func (c *FakeTFJobs) Apply(ctx context.Context, tFJob *kubefloworgv1.TFJobApplyConfiguration, opts metav1.ApplyOptions) (result *v1.TFJob, err error) {
	if tFJob == nil {
		return nil, fmt.Errorf("tFJob provided to Apply must not be nil")
	}
	data, err := json.Marshal(tFJob)
	if err != nil {
		return nil, err
	}
	name := tFJob.Name
	if name == nil {
		return nil, fmt.Errorf("tFJob.Name must be provided to Apply")
	}
	emptyResult := &v1.TFJob{}
	obj, err := c.Fake.
		Invokes(testing.NewPatchSubresourceActionWithOptions(tfjobsResource, c.ns, *name, types.ApplyPatchType, data, opts.ToPatchOptions()), emptyResult)

	if obj == nil {
		return emptyResult, err
	}
	return obj.(*v1.TFJob), err
}

// ApplyStatus was generated because the type contains a Status member.
// Add a +genclient:noStatus comment above the type to avoid generating ApplyStatus().
func (c *FakeTFJobs) ApplyStatus(ctx context.Context, tFJob *kubefloworgv1.TFJobApplyConfiguration, opts metav1.ApplyOptions) (result *v1.TFJob, err error) {
	if tFJob == nil {
		return nil, fmt.Errorf("tFJob provided to Apply must not be nil")
	}
	data, err := json.Marshal(tFJob)
	if err != nil {
		return nil, err
	}
	name := tFJob.Name
	if name == nil {
		return nil, fmt.Errorf("tFJob.Name must be provided to Apply")
	}
	emptyResult := &v1.TFJob{}
	obj, err := c.Fake.
		Invokes(testing.NewPatchSubresourceActionWithOptions(tfjobsResource, c.ns, *name, types.ApplyPatchType, data, opts.ToPatchOptions(), "status"), emptyResult)

	if obj == nil {
		return emptyResult, err
	}
	return obj.(*v1.TFJob), err
}
