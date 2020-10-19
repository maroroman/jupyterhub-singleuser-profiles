import React, { useState } from 'react'
import './EnvVarForm.css'
import Form from 'react-bootstrap/Form'
import FormGroup from 'react-bootstrap/FormGroup'
import Button from 'react-bootstrap/Button'
import APICalls from '../../CustomElements/APICalls'
import VarForm from '../../CustomElements/VarForm'

class EnvVarForm extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            envvars: {},
            items: [],
            secrets: {},
        }
        this.API = new APICalls()
    }

    async updateVars() {
        var data = await this.API.APIGet(this.API._CMPATH)
        this.setState({envvars: data['env']},() => {console.log("Updated EnvVars")})
        this.renderForms()
    }

    componentDidMount() {
        this.updateVars()
    }

    onBlur(e) {
        console.log("Entered Blur", e.target)
        var container = document.getElementById('EnvVarContainer')
        var vars = {}
        for (var i = 0; i < container.children.length; i++) {
            var keyValuePair = container.children[i]
            var key = keyValuePair.children[0].children[0].children[0] //should be rewritten
            var value = keyValuePair.children[0].children[1]
            console.log("BLUR key value: ", key, value)
            if (key.value) {
                if (value.value) {
                    vars[key.value] = value.value
                }
                else {
                    if (value.placeholder === "&#9679;&#9679;&#9679;&#9679;&#9679;") {  // is a password
                        vars[key.value] = this.state.secrets[key.value]
                    }
                    else {
                        vars[key.value] = value.placeholder
                    }
                }
            }
            else {
                if (value.value) {
                    vars[key.placeholder] = value.value
                }
                else {
                    if (value.placeholder === "&#9679;&#9679;&#9679;&#9679;&#9679;") {  // is a password
                        vars[key.placeholder] = this.state.secrets[key.placeholder]
                    }
                    else {
                        vars[key.placeholder] = value.placeholder
                    } 
                }
            }
        }
        this.setState({envvars: vars}, function() {this.sendVars()})
    }

    removeForm(e) {
        var parent = e.target.parentElement
        parent.remove()
        this.onBlur()
    }

    makeFormItem(key, value) {
        const newItem = [
            <div onBlur={(e) => this.onBlur(e)} className="VarGridDiv">
                <VarForm var_key={key} value={value} blurFunc={this.onBlur}/>
            </div>,
            <Button className="InnerGap" variant='danger' onClick={(e) => this.removeForm(e)}>
                Remove
            </Button>
        ]
        return newItem
    }

    addForm(e){
        //Frequently used variables could also be entered as a list if there are too many of them.
        var newItem = this.makeFormItem('variable_name', 'variable_value')
        this.setState(previousState => ({
            items: [...previousState.items, newItem]
        }));
        
    }

    renderForms() {
        console.log('Logging envvars:', this.state.envvars)
        for (const [key, value] of Object.entries(this.state.envvars)) {
            console.log("Generating: ", key, value)
            var newItem = this.makeFormItem(key, value)
            this.setState(previousState => ({
                items: [...previousState.items, newItem]
            }), () => {console.log("Rendered item", key, value)});
        }
    }

    async sendVars(){
        var json = JSON.stringify({env: this.state.envvars})
        var response = await this.API.APIPost(this.API._CMPATH, json)
    }

    render () {
        return (
            <Form className="EnvVarAccord">
                <Form.Label className="EnvVarForm">Environment Variables</Form.Label>
                <Form>
                    <FormGroup id='EnvVarContainer'>
                        {this.state.items.map(item => (
                                <Form.Row className="RowGap">{item}</Form.Row>
                        ))}
                    </FormGroup>
                    <Button variant='primary' onClick={(e) => this.addForm(e)}>
                        Add
                    </Button>
                </Form>
            </Form>
        )
    }

}

export default EnvVarForm
