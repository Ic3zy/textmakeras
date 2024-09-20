const express = require('express');
const { Builder, By, until } = require('selenium-webdriver');

const app = express();

app.get('/photooxy', async (req, res) => {
    const userText = req.query.text;
    const targetUrl = req.query.url;

    if (!targetUrl) {
        return res.status(400).json({ status: 'error', message: 'URL is required' });
    }

    let driver = await new Builder().forBrowser('chrome').build();

    try {
        await driver.get(targetUrl);
        await driver.executeScript(`
            const inputText = document.querySelector('input[name="text[]"]');
            inputText.value = "${userText}";
            const submitButton = document.querySelector('input[type="submit"]');
            submitButton.click();
        `);
        
        let linkImage = await driver.wait(until.elementLocated(By.id('link-image')), 10000);
        let linkImageText = await linkImage.getText();

        res.json({ link_image_text: linkImageText });
    } catch (err) {
        res.status(500).json({ status: 'error', message: err.message });
    } finally {
        await driver.quit();
    }
});

app.listen(5000, () => {
    console.log('Server is running on port 5000');
});
